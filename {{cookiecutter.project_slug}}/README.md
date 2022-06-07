# {{ cookiecutter.pkg_name }}
> Short blurb about what your product does.


[![PyPI][pypi-image]][pypi-url]
[![Downloads][downloads-image]][downloads-url]
[![Status][status-image]][pypi-url]
[![Python Version][python-version-image])][pypi-url]
[![tests][tests-image]][tests-url]
[![Codecov][codecov-image]][codecov-url]
[![CodeQL](https://github.com/Stephen-RA-King/{{cookiecutter.github_username}}/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Stephen-RA-King/{{cookiecutter.github_username}}/actions/workflows/codeql-analysis.yml)
[![readthedocs][readthedocs-image]][readthedocs-url]
{% if cookiecutter.use_pre_commit == 'y' -%}
[![pre-commit][pre-commit-image]][pre-commit-url]
{%- endif %}
{% if cookiecutter.use_isort == 'y' -%}
[![Imports: isort][isort-image]][isort-url]
{%- endif %}
{% if cookiecutter.use_black == 'y' -%}
[![Code style: black][black-image]][black-url]
{%- endif %}
{% if cookiecutter.use_mypy == 'y' -%}
[![Checked with mypy][mypy-image]][mypy-url]
{%- endif %}
{% if cookiecutter.use_bandit == 'y' -%}
[![security: bandit][bandit-image]][bandit-url]
{%- endif %}
{% if cookiecutter.use_commitizen == 'y' -%}
[![Commitizen friendly][commitizen-image]][commitizen-url]
{%- endif %}
[![License][license-image]][license]


One to two paragraph statement about your product and what it does.

![](assets/header.png)

## Installation

OS X & Linux:

```sh
pip3 install {{ cookiecutter.pkg_name }}
```

Windows:

```sh
pip install {{ cookiecutter.pkg_name }}
```

## Usage example

A few motivating and useful examples of how your product can be used. Spice this up with code blocks and potentially more screenshots.

_For more examples and usage, please refer to the [Wiki][wiki]._

## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
pip install --editable {{ cookiecutter.pkg_name }}
```



## Documentation
[**Read the Docs**](https://{{ cookiecutter.pkg_name }}.readthedocs.io/en/latest/)


## Meta
{% if cookiecutter.github_username == 'Stephen-RA-King' -%}
[![](assets/linkedin.png)](https://linkedin.com/in/stephen-k-3a4644210)
[![](assets/github.png)](https://github.com/Stephen-RA-King)
[![](assets/pypi.png)](https://pypi.org/project/{{ cookiecutter.pkg_name }}/)
[![](assets/www.png)](https://www.Stephen-RA-King)
[![](assets/email.png)](mailto:stephen.ra.king@gmail.com)
{% else %}
[![](assets/github.png)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.pkg_name }})
[![](assets/pypi.png)](https://pypi.org/project/{{ cookiecutter.pkg_name }}/)
{% endif %}

{{cookiecutter.author_name}} : {{cookiecutter.email}}

Distributed under the {{cookiecutter.license}} License. See [![License][license-image]][license] for more information.

[https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.pkg_name }}](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.pkg_name }})



<!-- Markdown link & img dfn's -->
[pypi-url]: https://pypi.org/project/{{ cookiecutter.pkg_name }}/
[pypi-image]: https://img.shields.io/pypi/v/{{cookiecutter.pkg_name}}.svg
[downloads-image]: https://static.pepy.tech/personalized-badge/{{cookiecutter.pkg_name}}?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads
[downloads-url]: https://pepy.tech/project/{{cookiecutter.pkg_name}}
[status-image]: https://img.shields.io/pypi/status/{{cookiecutter.pkg_name}}.svg
[python-version-image]: https://img.shields.io/pypi/pyversions/{{cookiecutter.pkg_name}}
[tests-image]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.pkg_name}}/actions/workflows/tests.yml/badge.svg
[tests-url]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.pkg_name}}/actions/workflows/tests.yml
[codeql-image]: https://github.com/Stephen-RA-King/{{cookiecutter.github_username}}/actions/workflows/codeql-analysis.yml/badge.svg
[codeql-url]: https://github.com/Stephen-RA-King/{{cookiecutter.github_username}}/actions/workflows/codeql-analysis.yml
[codecov-image]: https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.pkg_name}}/branch/main/graph/badge.svg
[codecov-url]: https://app.codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.pkg_name }}
[license]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.pkg_name }}/blob/main/LICENSE
[licence-image]: https://img.shields.io/pypi/l/{{cookiecutter.pkg_name}}
{% if cookiecutter.use_commitizen == 'y' -%}
[commitizen-image]: https://img.shields.io/badge/commitizen-friendly-brightgreen.svg
[commitizen-url]: http://commitizen.github.io/cz-cli/
{%- endif %}
[readthedocs-image]: https://readthedocs.org/projects/{{ cookiecutter.pkg_name }}/badge/?version=latest
[readthedocs-url]: https://{{ cookiecutter.pkg_name }}.readthedocs.io/en/latest/?badge=latest
{% if cookiecutter.use_pre_commit == 'y' -%}
[pre-commit-image]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit-url]: https://github.com/pre-commit/pre-commit
{%- endif %}
{% if cookiecutter.use_isort == 'y' -%}
[isort-image]: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
[isort-url]: https://pycqa.github.io/isort/
{%- endif %}
{% if cookiecutter.use_black == 'y' -%}
[black-image]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-url]: https://github.com/psf/black
{%- endif %}
{% if cookiecutter.use_bandit == 'y' -%}
[bandit-image]: https://img.shields.io/badge/security-bandit-yellow.svg
[bandit-url]: https://github.com/PyCQA/bandit
{%- endif %}
{% if cookiecutter.use_mypy == 'y' -%}
[mypy-image]: http://www.mypy-lang.org/static/mypy_badge.svg
[mypy-url]: http://mypy-lang.org/
{%- endif %}
[wiki]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.pkg_name }}/wiki
