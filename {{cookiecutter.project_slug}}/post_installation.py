import keyring
import json
from base64 import b64encode
import requests
from nacl import encoding, public
import json
from base64 import b64encode

import keyring
import requests
from nacl import encoding, public

GITHUB_TOKEN = keyring.get_password("github", "token")
TEST_PYPI_TOKEN = keyring.get_password("testpypi", "token")
PYPI_TOKEN = keyring.get_password("pypi", "token")
READTHEDOCS_TOKEN = keyring.get_password("readthedocs", "token")


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
        The service identifier. e.g. GitHub or readthedocs etc
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
    body_json = {
        "name": "{{ cookiecutter.pkg_name }}",
        "description": "{{ cookiecutter.project_short_description }}"
    }

    url = 'https://api.github.com/user/repos'
    header = {'Authorization': f'token {GITHUB_TOKEN}'}
    response = requests.post(
        url,
        json=body_json,
        headers=header,
    )
    print(response.json())


def github_create_secret(secret_name: str, secret_value: str) -> None:
    url_public_key = "https://api.github.com/repos/{{ cookiecutter.github_username }}" \
                     "/{{ cookiecutter.pkg_name }}/actions/secrets/public-key"

    authorization = f"token {GITHUB_TOKEN}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": authorization,
    }

    r = requests.get(
        url=url_public_key,
        headers=headers
    )

    if r.status_code == 200:
        key_datas = r.json()
        url_secret = f"https://api.github.com/repos/{{ cookiecutter.github_username }}" \
                     f"/{{ cookiecutter.pkg_name }}/actions/secrets/{secret_name}"

        data = {"encrypted_value": encrypt(key_datas["key"], secret_value),
                "key_id": key_datas["key_id"]}

        json_data = json.dumps(data)

        r = requests.put(
            url=url_secret,
            data=json_data,
            headers=headers
        )

        if r.status_code == 201 or r.status_code == 204:
            print(
                f"✅ Secret {secret_name} successfully added ")

        else:
            print("❌ Couldn't add the secret to the repository")
            print(r.status_code, r.reason)

    else:
        print("❌ Couldn't get the repository public key")
        print(r.status_code, r.reason)


def readthedocs_create() -> None:
    body_json = {
        "name": "{{ cookiecutter.pkg_name }}",
        "repository": {
            "url": "https://github.com/{{ cookiecutter.github_username }}"
                   "/{{ cookiecutter.pkg_name }}",
            "type": "git"
        },
        "homepage": "http://template.readthedocs.io/",
        "programming_language": "py",
        "default_branch": "main",
        "language": "en"
    }

    url = 'https://readthedocs.org/api/v3/projects/'
    header = {'Authorization': f'token {READTHEDOCS_TOKEN}'}
    response = requests.post(
        url,
        json=body_json,
        headers=header,
    )
    print(response.json())


def readthedocs_update() -> None:
    body_json = {
        "name": "{{ cookiecutter.pkg_name }}",
        "default_branch": "main"
    }

    url = 'https://readthedocs.org/api/v3/projects/'
    header = {'Authorization': f'token {READTHEDOCS_TOKEN}'}
    response = requests.post(
        url,
        json=body_json,
        headers=header,
    )
    print(response.json())


def main() -> None:
    github_create_repo()
    github_create_secret("TEST_PYPI_API_TOKEN", TEST_PYPI_TOKEN)
    github_create_secret("PYPI_API_TOKEN", TEST_PYPI_TOKEN)
    readthedocs_create()


if __name__ == "__main__":
    main()
    # readthedocs_update()
