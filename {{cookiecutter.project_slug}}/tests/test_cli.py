"""

"""
from click.testing import CliRunner

from src.myapp import cli


def test_author():
    runner = CliRunner()
    result = runner.invoke(cli.author)
    assert result.exit_code == 0
    assert result.output == 'Author name: {{ cookiecutter.author_name }}\n'


def test_author_verbose():
    runner = CliRunner()
    result = runner.invoke(cli.author, ["--verbose"])
    assert result.exit_code == 0
    assert result.output == 'Author name: {{ cookiecutter.author_name }}\n' \
                            'Author eMail: {{ cookiecutter.email }}\n'


def test_author_help():
    runner = CliRunner()
    result = runner.invoke(cli.author, ["--help"])
    assert result.exit_code == 0
    assert "  Display Author Name" in result.output


def test_pkg_info():
    runner = CliRunner()
    result = runner.invoke(cli.pkg_info)
    assert result.exit_code == 0
    assert result.output == 'Package Version: {{ cookiecutter.version }}\n'


def test_pkg_info_help():
    runner = CliRunner()
    result = runner.invoke(cli.pkg_info, ["--help"])
    assert result.exit_code == 0
    assert "  Display Package Information" in result.output
