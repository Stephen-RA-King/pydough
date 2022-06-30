"""
Tasks for maintaining the project.

Execute 'invoke --list' for guidance on using Invoke
"""
# Core Library modules
import logging
import logging.config
import shutil
import webbrowser
from pathlib import Path

# Third party modules
import yaml  # type: ignore
from invoke import task
from jinja2 import Template

ROOT_DIR = Path(__file__).parent
BUILD_FROM = "".join(['"', str(ROOT_DIR / "."), '"'])
DIST_SOURCE = "".join(['"', str(ROOT_DIR / "dist/*"), '"'])
PYPIRC = "".join(['"', str(ROOT_DIR / ".pypirc"), '"'])

DOC_DIR_STR = "".join(['"', str(ROOT_DIR / "docs"), '"'])
DOCS_BUILD_DIR_STR = "".join(['"', str(ROOT_DIR / "docs" / "_build"), '"'])
DOCS_INDEX = "".join(['"', str(ROOT_DIR / "docs" / "_build" / "index.html"), '"'])


LOG_DIR = ROOT_DIR.joinpath("logs")
TEST_DIR = ROOT_DIR.joinpath("tests")
SRC_DIR = ROOT_DIR.joinpath("src")
PKG_DIR = SRC_DIR.joinpath("{{ cookiecutter.pkg_name }}")

PYTHON_FILES_ALL = list(ROOT_DIR.rglob("*.py"))
PYTHON_FILES_ALL.remove(ROOT_DIR / "tasks.py")
PYTHON_FILES_ALL_STR = ""
for item in PYTHON_FILES_ALL:
    PYTHON_FILES_ALL_STR = "".join([PYTHON_FILES_ALL_STR, '"', str(item), '" '])

PYTHON_FILES_SRC = list(SRC_DIR.rglob("*.py"))
PYTHON_FILES_SRC_STR = ""
for item in PYTHON_FILES_SRC:
    PYTHON_FILES_SRC_STR = "".join([PYTHON_FILES_SRC_STR, '"', str(item), '" '])

if LOG_DIR / "tasks.log":
    Path.unlink(LOG_DIR / "tasks.log", missing_ok=True)

LOGGING_CONFIG_TEMPLATE = """
version: 1
disable_existing_loggers: False

formatters:
  basic:
    style: "{"
    format: "{levelname:s}:{name:s}:{message:s}"
  timestamp:
    style: "{"
    format: "{asctime} - {levelname} - {name} - {message}"
    datefmt: "%Y-%m-%d+%H:%M:%S"

handlers:
  console:
    class: logging.StreamHandler
    level: INFO
    stream: ext://sys.stdout
    formatter: basic
  file:
    class: logging.FileHandler
    level: DEBUG
    filename: {{ LOG_FILE }}
    encoding: utf-8
    formatter: timestamp

loggers:
  main:
    handlers: [console, file]
    level: DEBUG
    propagate: False
"""

LOGGING_CONFIG = Template(LOGGING_CONFIG_TEMPLATE).render(
    LOG_FILE=str(LOG_DIR / "tasks.log")
)
logging.config.dictConfig(yaml.safe_load(LOGGING_CONFIG))
logger = logging.getLogger("main")

logger.debug(f"Total python files: {len(PYTHON_FILES_ALL)} ")
for item in PYTHON_FILES_ALL:
    logger.debug(f"{item}")
logger.debug(f"src python files: {len(PYTHON_FILES_SRC)}")
for item in PYTHON_FILES_SRC:
    logger.debug(f"{item}")


def _delete_director(items_to_delete):
    """Utility function to delete files or directories."""
    for item in items_to_delete:
        if item.is_dir():
            logger.debug(f"Deleting Directory: {item}")
            shutil.rmtree(item, ignore_errors=True)
        elif item.is_file():
            logger.debug(f"Deleting File: {item}")
            Path.unlink(item, missing_ok=True)
        else:
            raise ValueError(f"{item} is not a directory or a file")


def _finder(directory, item, exclusions):
    """Utility function to generate a Path list of files based on globs."""
    item_list = list(directory.rglob(item))
    logger.debug(f"for {item}: Found: {item_list}")
    for exc in exclusions:
        logger.debug(f"removing exclusion: {exc}")
        if exc in item_list:
            item_list.remove(exc)
    if item_list:
        logger.debug(f"Items to process: {item_list}")
        _delete_director(item_list)


def _run(c, command):
    return c.run(command)


@task()
def clean_mypy(c):
    """Clean up mypy cache and results."""
    patterns = [
        ".mypy_cache",
        "mypy-report",
    ]
    excludes = []
    for pattern in patterns:
        _finder(ROOT_DIR, pattern, excludes)


@task()
def clean_build(c):
    """Clean up build artifacts."""
    # Specify glob patterns to delete
    patterns = [
        "build/",
        "dist/",
        ".eggs/",
        "*egg-info",
        "*.egg",
    ]
    # specify pathlib objects to exclude from deletion (can be directories of files)
    excludes = [
        SRC_DIR / "{{ cookiecutter.pkg_name }}.egg-info/",
    ]
    for pattern in patterns:
        _finder(ROOT_DIR, pattern, excludes)


@task()
def clean_test(c):
    """Clean up test artifacts."""
    patterns = [
        ".pytest_cache",
        "htmlcov",
        ".coverage",
        "coverage.xml",
        "pytest-report.html",
    ]
    excludes = []
    for pattern in patterns:
        _finder(ROOT_DIR, pattern, excludes)


@task()
def clean_python(c):
    """Clean up python file artifacts."""
    patterns = ["*.pyc", "*.pyo" "__pycache__"]
    excludes = []
    for pattern in patterns:
        _finder(ROOT_DIR, pattern, excludes)


@task()
def clean_docs(c):
    """Clean the document build."""
    patterns = ["_build", "jupyter_execute", "*.css"]
    excludes = []
    for pattern in patterns:
        _finder(ROOT_DIR, pattern, excludes)


@task()
def clean_logs(c):
    """Clean the log files."""
    patterns = ["*.log"]
    excludes = [
        LOG_DIR / "tasks.log",
    ]
    for pattern in patterns:
        _finder(ROOT_DIR, pattern, excludes)


@task()
def clean_bandit(c):
    """Clean the bandit report files."""
    patterns = ["bandit.html"]
    excludes = []
    for pattern in patterns:
        _finder(ROOT_DIR, pattern, excludes)


@task(
    pre=[
        clean_mypy,
        clean_build,
        clean_python,
        clean_test,
        clean_docs,
        clean_logs,
        clean_bandit,
    ]
)
def clean(c):
    """Run all clean sub-tasks."""


@task(
    name="lint-isort",
    help={
        "check": "Checks if source is formatted without applying changes",
        "src": "Select the files to be checked. Default is all only",
    },
)
def lint_isort(c, check=False, src=False):
    """Run isort against selected python files."""
    isort_options = ["--check-only", "--diff"] if check else []
    if src:
        c.run(f"isort {' '.join(isort_options)} {PYTHON_FILES_SRC_STR}")
    else:
        c.run(f"isort {' '.join(isort_options)} {PYTHON_FILES_ALL_STR}")


@task(
    name="lint-black",
    help={
        "check": "Checks if source is formatted without applying changes",
        "src": "Select the files to be checked. Default is all only",
    },
)
def lint_black(c, check=False, src=False):
    """Runs black formatter against selected python files."""
    black_options = ["--diff", "--check"] if check else []
    if src:
        c.run(f"black {' '.join(black_options)} {PYTHON_FILES_SRC_STR}")
    else:
        c.run(f"black {' '.join(black_options)} {PYTHON_FILES_ALL_STR}")


@task(
    name="lint-flake8",
    help={"src": "Select the files to be checked. Default is all only"},
)
def lint_flake8(c, src=False):
    """Run flake8 against selected files."""
    if src:
        c.run(f"flake8 {PYTHON_FILES_SRC_STR}")
    else:
        c.run(f"flake8 {PYTHON_FILES_ALL_STR}")


@task(pre=[lint_isort, lint_black, lint_flake8])
def lint(c):
    """Run all lint tasks."""


@task(
    pre=[clean_mypy],
    help={
        "open_browser": "Open the mypy report in the web browser",
        "src": "Select the files to be checked. Default is all only",
    },
)
def mypy(c, open_browser=False, src=False):
    """Run mypy against selected python files."""
    if src:
        c.run(f"mypy {PYTHON_FILES_SRC_STR}")
    else:
        c.run(f"mypy {PYTHON_FILES_ALL_STR}")
    if open_browser:
        report_path = "".join(['"', str(ROOT_DIR / "mypy-report" / "index.html"), '"'])
        webbrowser.open(report_path)


@task
def safety(c):
    """Runs safety to check for insecure requirements."""
    c.run("safety check --full-report")


@task(
    name="bandit",
    help={
        "open_browser": "Open the bandit report in the web browser",
        "src": "Select the files to be checked. Default is all only",
    },
)
def bandit(c, open_browser=False, src=False):
    """Runs bandit against selected python files."""
    bandit_options = ["--format html", "--output bandit.html", "--skip B101,B603"]
    if src:
        c.run(f"bandit {' '.join(bandit_options)} {PYTHON_FILES_SRC_STR}")
    else:
        c.run(f"bandit {' '.join(bandit_options)} {PYTHON_FILES_ALL_STR}")
    if open_browser:
        report_path = "".join(['"', str(ROOT_DIR / "bandit.html"), '"'])
        webbrowser.open(report_path)


@task(pre=[safety, bandit])
def secure(c):
    """Runs all security tools."""


@task(
    pre=[clean_test],
    help={
        "open_browser": "Open the test report in the web browser",
    },
)
def tests(c, open_browser=False):
    """Run tests using pytest."""
    print(TEST_DIR)
    c.run(
        f'pytest "{str(TEST_DIR)}" --cov={{ cookiecutter.pkg_name }} --cov-report=html '
        f"--html=pytest-report.html"
    )
    if open_browser:
        pytest_path = "".join(['"', str(ROOT_DIR / "pytest-report.html"), '"'])
        cov_path = "".join(['"', str(ROOT_DIR / "htmlcov" / "index.html"), '"'])
        webbrowser.open(pytest_path)
        webbrowser.open(cov_path)


@task(
    pre=[clean_docs],
    help={
        "open_browser": "Open  the docs in the web browser",
    },
)
def docs(c, open_browser=False):
    """Build documentation."""
    build_docs = f"sphinx-build -b html {DOC_DIR_STR} {DOCS_BUILD_DIR_STR}"
    c.run(build_docs)
    if open_browser:
        webbrowser.open(DOCS_INDEX)


@task(pre=[clean_build])
def build(c):
    """Creates a new sdist & wheel build using the PyPA tool."""
    c.run(f"python -m build --sdist --wheel {BUILD_FROM}")


@task(pre=[build])
def pypi_test(c):
    """Uploads a build to the PyPI-test python repository."""
    c.run(f"python -m twine upload --config-file {PYPIRC} -r testpypi {DIST_SOURCE}")


@task(pre=[build])
def pypi(c):
    """Uploads a build to the PyPI python repository."""
    c.run(f"python -m twine upload --config-file {PYPIRC} {DIST_SOURCE}")


@task(pre=[pypi, pypi_test])
def publish(c):
    """Uploads a build to the PyPI-test and PyPI python repositories."""


@task
def psr(c):
    """Runs semantic-release publish."""
    c.run("semantic-release publish")
