# Core Library modules
import argparse
import json
import logging.config
import os
import subprocess
import sys
from base64 import b64encode
from pathlib import Path
from typing import Any
import webbrowser

# Third party modules
import keyring
import requests  # type: ignore
import yaml
from nacl import encoding, public

PLATFORM = sys.platform
SLUG_DIR = Path.cwd()
LOG_DIR = SLUG_DIR / "logs"
GITHUB_TOKEN = keyring.get_password("github", "token")
TEST_PYPI_TOKEN = keyring.get_password("testpypi", "token")
PYPI_TOKEN = keyring.get_password("pypi", "token")
READTHEDOCS_TOKEN = keyring.get_password("readthedocs", "token")
DEV_DIR = r"D:\PYTHON PROJECT\PROJECTS\DEV"
VIRTUALENV_DIR = r"D:\PYTHON PROJECT\PROJECTS\VIRTUALENVS"


LOGGING_CONFIG = """
version: 1
disable_existing_loggers: False
handlers:
  console:
    class: logging.StreamHandler
    level: INFO
    stream: ext://sys.stdout
    formatter: basic
  file:
    class: logging.FileHandler
    level: DEBUG
    filename: logs/post_install.log
    encoding: utf-8
    formatter: timestamp

formatters:
  basic:
    style: "{"
    format: "{message:s}"
  timestamp:
    style: "{"
    format: "{asctime} - {levelname} - {name} - {message}"

loggers:
  post:
    handlers: [console, file]
    level: DEBUG
    propagate: False
"""

logging.config.dictConfig(yaml.safe_load(LOGGING_CONFIG))
logger = logging.getLogger("post")

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--refresh", help="refresh the post installation procedure",
                    action="store_true")
options = parser.parse_args()


def execute(*args: str, supress_exception: bool = False, cwd: Any = None) -> Any:
    logger.debug(f"Executing command line: '{args}'")
    cur_dir = os.getcwd()
    logger.debug(f"Current Directory: {cur_dir}")
    try:
        if cwd:
            logger.debug(f"Changing Directory to: {cwd}")
            os.chdir(cwd)
        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()
        decoded_out = out.decode("utf-8")
        decoded_err = err.decode("utf-8")
        if err and not supress_exception:
            logger.exception(decoded_err)
            raise Exception(decoded_err)
        else:
            return decoded_out
    finally:
        logger.debug(f"Changing Directory to: {cur_dir}")
        os.chdir(cur_dir)


def encrypt(public_key: str, secret_value: str) -> str:
    """Encrypt a Unicode string using the public key."""
    public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return b64encode(encrypted).decode("utf-8")


def set_keyring(service: str, id_type: str, hidden: str) -> None:
    """Encrypt a service ID or Password

    Parameters
    ----------
    service: str
        The service identifier. e.g. GitHub or readthedocs etc.
    id_type: str
        what is being encrypted. e.g. and "ID" or "Password"
    hidden: str
        The actual string to encrypt and hide on the keyring

    Examples
    --------
    keyring.set_password("gmail", "service_id", "contact.me@gmail.com")
    keyring.set_password("gmail", "service_password", "P@55w0rd1")
    """
    keyring.set_password(service, id_type, hidden)


def github_create_repo() -> None:
    logger.info("\nCreating GitHub repository")
    body_json = {"name": "{{ cookiecutter.project_name }}", "description": "placeholder"}

    url = "https://api.github.com/user/repos"
    header = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.post(
        url,
        json=body_json,
        headers=header,
    )
    if response.status_code == 201:
        logger.info(".... OK")
    else:
        logger.info(f".... FAILED: {response.status_code}")


def github_create_secret(secret_name: str, secret_value: str) -> None:
    logger.info(f"\nGitHub action secret creation - {secret_name}")
    url_public_key = (
        "https://api.github.com/repos/Stephen-RA-King"
        "/{{ cookiecutter.project_name }}/actions/secrets/public-key"
    )

    authorization = f"token {GITHUB_TOKEN}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": authorization,
    }

    r = requests.get(url=url_public_key, headers=headers)

    if r.status_code == 200:
        key_datas = r.json()
        url_secret = (
            f"https://api.github.com/repos/"
            f"Stephen-RA-King"
            f"/{{ cookiecutter.project_name }}/actions/secrets/{secret_name}"
        )

        data = {
            "encrypted_value": encrypt(key_datas["key"], secret_value),
            "key_id": key_datas["key_id"],
        }

        json_data = json.dumps(data)

        r = requests.put(url=url_secret, data=json_data, headers=headers)

        if r.status_code in (201, 204):
            logger.info(".... OK")

        else:
            logger.info(".... FAILED")
            logger.info(r.status_code, r.reason)

    else:
        logger.info("Couldn't get the repository public key")
        logger.info(r.status_code, r.reason)


def readthedocs_create() -> None:
    logger.info("\nCreating ReadTheDocs project")
    body_json = {
        "name": "{{ cookiecutter.project_name }}",
        "repository": {
            "url": "https://github.com/Stephen-RA-King" "/{{ cookiecutter.project_name }}",
            "type": "git",
        },
        "homepage": "http://template.readthedocs.io/",
        "programming_language": "py",
        "default_branch": "main",
        "language": "en",
    }

    url = "https://readthedocs.org/api/v3/projects/"
    header = {"Authorization": f"token {READTHEDOCS_TOKEN}"}
    response = requests.post(
        url,
        json=body_json,
        headers=header,
    )
    if response.status_code == 201:
        logger.info(".... OK")
    else:
        logger.info(".... FAILED")


def readthedocs_update() -> None:
    # https://docs.readthedocs.io/en/stable/api/v3.html#project-update
    logger.info("\nUpdating Read the docs project with chosen git branch")
    body_json = {
        "name": "{{ cookiecutter.project_name }}",
        "repository": {
            "url": "https://github.com/Stephen-RA-King" "/{{ cookiecutter.project_name }}",
            "type": "git",
        },
        "homepage": "http://template.readthedocs.io/",
        "programming_language": "py",
        "default_branch": "{{ cookiecutter.initial_git_branch_name }}",
        "language": "en",
    }

    url = "https://readthedocs.org/api/v3/projects/{{ cookiecutter.project_name }}/"
    header = {"Authorization": f"token {READTHEDOCS_TOKEN}"}
    response = requests.patch(
        url,
        json=body_json,
        headers=header,
    )
    if response.status_code == 204:
        logger.info(".... OK")
    else:
        logger.info(f".... FAILED - {response.status_code}")


def remove_modules() -> None:
    """Checks installed modules for modules listed to be removed."""
    remove_these_modules = [
        "arrow",
        "binaryornot",
        "chardet",
        "cookiecutter",
        "jinja2-time",
        "poyo",
        "python-dateutil",
        "python-slugify",
        "text-unidecode",
    ]
    for module in remove_these_modules:
        logger.info(f"........ Removing module {module}")
        current_list = execute(sys.executable, "-m", "pip", "freeze", "-q", "-l")
        if module in current_list:
            execute(
                sys.executable,
                "-m",
                "pip",
                "uninstall",
                "-y",
                "-q",
                module,
            )
        logger.info("............ OK")


def file_word_replace(filepath: str, old_word: str, new_word: str) -> None:
    with open(filepath) as file:
        file_data = file.read()
    file_data = file_data.replace(old_word, new_word)
    with open(filepath, "w") as file:
        file.write(file_data)


def main() -> None:
    if not options.refresh:
        github_create_repo()

        github_create_secret("PYPI_API_TOKEN", PYPI_TOKEN)
        github_create_secret("TEST_PYPI_API_TOKEN", TEST_PYPI_TOKEN)

    if not options.refresh:
        readthedocs_create()

    logger.info("\nUpdating .pypi file with secret tokens")
    file_word_replace(".pypirc", "token1", PYPI_TOKEN)
    file_word_replace(".pypirc", "token2", TEST_PYPI_TOKEN)
    logger.info(".... OK")

    logger.info("\nPatching Python semantic release package windows bug")
    file_path = r"\{{ cookiecutter.project_name }}\Lib\site-packages\semantic_release\repository.py"
    repository = "".join([VIRTUALENV_DIR, file_path])
    file_word_replace(repository, "~/.pypirc", ".pypirc")
    logger.info(".... OK")

    logger.info(
        "\nUpdating GitHub action tests.yml with chosen git branch & package name"
    )
    tests = r".github\workflows\tests.yml"
    file_word_replace(tests, "default-branch1", "{{ cookiecutter.initial_git_branch_name }}")
    file_word_replace(tests, "default-branch2", "{{ cookiecutter.initial_git_branch_name }}")
    file_word_replace(tests, "package_name", "{{ cookiecutter.project_name }}")
    logger.info(".... OK")

    logger.info("\nUpdating GitHub action codeql-analysis.yml with chosen git branch")
    codeql = r".github\workflows\codeql-analysis.yml"
    file_word_replace(codeql, "default-branch1", "{{ cookiecutter.initial_git_branch_name }}")
    file_word_replace(codeql, "default-branch2", "{{ cookiecutter.initial_git_branch_name }}")
    logger.info(".... OK")

    logger.info("\nInstalling requirements")
    execute("pip-sync", "requirements.txt")
    logger.info(".... OK")

    logger.info("\nChanging requirements from 'development' to 'test'")
    file_word_replace("requirements.txt", "development", "test")
    logger.info(".... OK")

    if not options.refresh:
        logger.info("\nInitial git add, commit & push")
        execute("git", "add", "assets/*")
        execute(
            "git", "commit", "-q", "-m", "chore: initial commit", supress_exception=True
        )
        execute("git", "push", "-q", "-u", "origin", "main")
        logger.info(".... OK")

    if not options.refresh:
        readthedocs_update()

    logger.info("\nInstalling the package as an 'editable' package locally")
    execute(sys.executable, "-m", "pip", "install", "-e", ".")
    logger.info(".... OK")

    message = (
        "\nSUCCESS! - ALL POST INSTALLATION TASKS ARE COMPLETE - "
        "this module can now be deleted"
    )
    logger.info(f"\n{'*' * (len(message) - 2)}")
    logger.info(message)
    logger.info(f"\n{'*' * len(message)}")

    logger.info("\n Final steps:")
    logger.info(f"{'=' * 14}")
    logger.info(
        "1 - Add the remaining files to git, commit and push\n"
        "2 - tag and push tags\n"
        "3 - Goto 'Codecov.io' and add the repository\n"
        "4 - Goto 'requires.io' and add the repository\n"
        "5 - Goto 'codefactor.io' and add the repository\n"
        "6 - Goto 'deepsource.io' and add the repository\n"
        "7 - Goto 'codeclimate.io' and add the repository\n"
    )
    webbrowser.open("https://app.codecov.io/login/gh?")
    webbrowser.open("https://requires.io/auth/github/login/?process=login&scope=repo")
    webbrowser.open("https://www.codefactor.io")
    webbrowser.open("https://deepsource.io/login")
    webbrowser.open("https://codeclimate.com/login/github/join")


if __name__ == "__main__":
    main()
