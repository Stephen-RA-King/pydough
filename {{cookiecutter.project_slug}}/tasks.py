"""
Tasks for maintaining the project.

Execute 'invoke --list' for guidance on using Invoke
"""
# Core Library modules
import logging.config
import shutil
import webbrowser
from pathlib import Path

# Third party modules
import yaml  # type: ignore
from invoke import task


ROOT_DIR = Path(__file__).parent
DOCS_DIR = ROOT_DIR.joinpath("docs")
DOCS_BUILD_DIR = DOCS_DIR.joinpath("_build")
DOCS_INDEX = DOCS_BUILD_DIR.joinpath("index.html")
LOG_DIR = ROOT_DIR.joinpath("logs")
TEST_DIR = ROOT_DIR.joinpath("tests")
SRC_DIR = ROOT_DIR.joinpath("src")
PKG_DIR = SRC_DIR.joinpath("{{ cookiecutter.pkg_name }}")
PYTHON_FILES_ALL = list(Path(".").rglob("*.py"))
PYTHON_FILES_ALL.remove(Path("tasks.py"))
PYTHON_FILES_ALL_STR = " ".join([str(p) for p in PYTHON_FILES_ALL])
PYTHON_FILES_SRC = list(Path("src").rglob("*.py"))
PYTHON_FILES_SRC_STR = " ".join([str(p) for p in PYTHON_FILES_SRC])

LOGGING_CONFIG = """
version: 1
disable_existing_loggers: False
handlers:
  console:
    class: logging.StreamHandler
    level: WARNING
    stream: ext://sys.stdout
    formatter: basic
  file:
    class: logging.FileHandler
    level: DEBUG
    filename: logs/tasks.log
    encoding: utf-8
    formatter: timestamp

formatters:
  basic:
    style: "{"
    format: "{levelname:s}:{name:s}:{message:s}"
  timestamp:
    style: "{"
    format: "{asctime} - {levelname} - {name} - {message}"

loggers:
  tasks:
    handlers: [console, file]
    level: DEBUG
    propagate: False
"""

logging.config.dictConfig(yaml.safe_load(LOGGING_CONFIG))
logger = logging.getLogger("tasks")


def _delete_director(items_to_delete):
    """Utility function to delete files or directories"""
    for item in items_to_delete:
        if item.is_dir():
            logger.info(f"Deleting Directory: {item}")
            shutil.rmtree(item, ignore_errors=True)
        elif item.is_file():
            logger.info(f"Deleting File: {item}")
            Path.unlink(item, missing_ok=True)
        else:
            raise ValueError(f"{item} is not a directory or a file")


def _finder(directory, item, exclusions):
    """Utility function to generate a Path list of files based on globs"""
    item_list = list(Path(directory).rglob(item))
    for exc in exclusions:
        if Path(exc) in item_list:
            item_list.remove(Path(exc))
    if item_list:
        _delete_director(item_list)


@task()
def clean_mypy(c):
    """Clean up mypy cache and results."""
    patterns = [
        ".mypy_cache",
        "mypy-report",
    ]
    excludes = []
    for pattern in patterns:
        _finder(".", pattern, excludes)


@task()
def clean_build(c):
    """Clean up build artifacts."""
    patterns = [
        "build/",
        "dist/",
        ".eggs/",
        "*egg-info",
        "*.egg",
    ]
    excludes = []
    for pattern in patterns:
        _finder(".", pattern, excludes)


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
        _finder(".", pattern, excludes)


@task()
def clean_python(c):
    """Clean up python file artifacts."""
    patterns = ["*.pyc", "*.pyo" "__pycache__"]
    excludes = []
    for pattern in patterns:
        _finder(".", pattern, excludes)


@task()
def clean_docs(c):
    """Clean the document build"""
    patterns = ["_build", "jupyter_execute", "*.css"]
    excludes = []
    for pattern in patterns:
        _finder(".", pattern, excludes)


@task()
def clean_logs(c):
    """Clean the log files"""
    patterns = ["*.log"]
    excludes = ["logs/tasks.log"]
    for pattern in patterns:
        _finder(".", pattern, excludes)


@task(pre=[clean_mypy, clean_build, clean_python, clean_test, clean_docs, clean_logs])
def clean(c):
    """Run all clean sub-tasks."""


@task(
    name="lint-isort",
    help={"check": "Checks if source is formatted without applying changes"},
)
def lint_isort(c, check=False):
    """Run isort against all python filoes"""
    isort_options = ["--check-only", "--diff"] if check else []
    c.run(f"isort {' '.join(isort_options)} {PYTHON_FILES_ALL_STR}")


@task(
    name="lint-black",
    help={"check": "Checks if source is formatted without applying changes"},
)
def lint_black(c, check=False):
    """Runs black formatter against all python files"""
    black_options = ["--diff", "--check"] if check else ["--quiet"]
    c.run(f"black {' '.join(black_options)} {PYTHON_FILES_ALL_STR}")


@task()
def lint_flake8(c):
    """Run flake8."""
    print(PYTHON_FILES_ALL_STR)
    c.run(f"flake8 {PYTHON_FILES_ALL_STR}")


@task(pre=[lint_isort, lint_black, lint_flake8])
def lint(c):
    """Run all lint tasks"""


@task(
    pre=[clean_mypy],
    help={
        "open_browser": "Open the mypy report in the web browser",
    },
)
def mypy(c, open_browser=False):
    """Run mypy against src python files."""
    c.run(f"mypy {PYTHON_FILES_SRC_STR}")
    if open_browser:
        webbrowser.open(r"mypy-report\index.html")


@task
def safety(c):
    """Runs safety to check for insecure requirements"""
    c.run("safety check --stdin --full-report")


@task
def bandit(c):
    """Runs Bandit security scanner against all python files"""
    c.run(f"bandit {PYTHON_FILES_ALL_STR}")


@task(pre=[safety, bandit])
def secure(c):
    """Runs all security tools"""


@task(
    pre=[clean_test],
    help={
        "open_browser": "Open the test report in the web browser",
    },
)
def tests(c, open_browser=False):
    """Run tests using pytest."""
    print(TEST_DIR)
    c.run("pytest --cov={{ cookiecutter.pkg_name }} --cov-report=html --html=pytest-report.html")
    if open_browser:
        webbrowser.open("pytest-report.html")


@task(
    pre=[clean_docs],
    help={
        "open_browser": "Open  the docs in the web browser",
    },
)
def docs(c, open_browser=False):
    """Build documentation."""
    c.run("sphinx-build -b html docs docs/_build")
    if open_browser:
        webbrowser.open(DOCS_INDEX.absolute().as_uri())


@task(pre=[clean_build])
def build(c):
    """Creates a new sdist & wheel build using the PyPA tool"""
    c.run("python -m build --sdist --wheel .")


@task(pre=[build])
def pypi_test(c):
    """Uploads a build to the PyPI-test python repository"""
    c.run("python -m twine upload --config-file .pypirc -r testpypi dist/*")


@task(pre=[build])
def pypi(c):
    """Uploads a build to the PyPI python repository"""
    c.run("python -m twine upload --config-file .pypirc dist/*")


@task(pre=[pypi, pypi_test])
def publish(c):
    """Uploads a build to the PyPI-test and PyPI python repositories"""


@task
def psr(c):
    """Runs semantic-release publish"""
    c.run("semantic-release publish")
