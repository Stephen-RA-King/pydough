# {{ cookiecutter.pkg_name }}

> Short blurb about what your product does.

[![PyPI][pypi-image]][pypi-url]
[![Downloads][downloads-image]][downloads-url]
[![Status][status-image]][pypi-url]
[![Python Version][python-version-image]][pypi-url]
[![Format][format-image]][pypi-url]
[![Requirements][requirements-status-image]][requirements-status-url]
[![tests][tests-image]][tests-url]
[![Codecov][codecov-image]][codecov-url]
[![CodeFactor][codefactor-image]][codefactor-url]
[![Codeclimate][codeclimate-image]][codeclimate-url]
[![Lgtm alerts][lgtm-alerts-image]][lgtm-alerts-url]
[![Lgtm quality][lgtm-quality-image]][lgtm-quality-url]
[![CodeQl][codeql-image]][codeql-url]
[![readthedocs][readthedocs-image]][readthedocs-url]
{% if cookiecutter.use_pre_commit == 'y' -%}
[![pre-commit][pre-commit-image]][pre-commit-url]
[![pre-commit.ci status][pre-commit.ci-image]][pre-commit.ci-url]
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
[![Conventional Commits][conventional-commits-image]][conventional-commits-url]
[![DeepSource][deepsource-image]][deepsource-url]
[![license][license-image]][license-url]

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

### - [**Read the Docs**](https://{{ cookiecutter.pkg_name }}.readthedocs.io/en/latest/)

### - [**Wiki**](https://github.com/Stephen-RA-King/{{ cookiecutter.pkg_name }}/wiki)

## Meta
{% if cookiecutter.github_username == 'Stephen-RA-King' -%}
[![](assets/linkedin.png)](https://linkedin.com/in/stephen-k-3a4644210)
[![](assets/github.png)](https://github.com/Stephen-RA-King)
[![](assets/pypi.png)](https://pypi.org/project/{{ cookiecutter.pkg_name }}/)
[![](assets/www.png)](https://www.justpython.tech)
[![](assets/email.png)](mailto:stephen.ra.king@gmail.com)
[![](assets/cv.png)](https://www.justpython.tech/cv) 
{% else %}
[![](assets/github.png)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.pkg_name }})
[![](assets/pypi.png)](https://pypi.org/project/{{ cookiecutter.pkg_name }}/)
{% endif %}

{{cookiecutter.author_name}} : {{cookiecutter.email}}

Distributed under the {{cookiecutter.license}} license. See [license](license-url) for more information.

[https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.pkg_name }}](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.pkg_name }})

<!-- Markdown link & img dfn's -->

{% if cookiecutter.use_bandit == 'y' -%}
[bandit-image]: https://img.shields.io/badge/security-bandit-yellow.svg
[bandit-url]: https://github.com/PyCQA/bandit
{%- endif %}
{% if cookiecutter.use_black == 'y' -%}
[black-image]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-url]: https://github.com/psf/black
{%- endif %}
[codeclimate-image]: https://api.codeclimate.com/v1/badges/7fc352185512a1dab75d/maintainability
[codeclimate-url]: https://codeclimate.com/github/{{cookiecutter.github_username}}/{{cookiecutter.pkg_name}}/maintainability
[codecov-image]: https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.pkg_name}}/branch/main/graph/badge.svg
[codecov-url]: https://app.codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.pkg_name }}
[codefactor-image]: https://www.codefactor.io/repository/github/Stephen-RA-King/{{ cookiecutter.pkg_name }}/badge
[codefactor-url]: https://www.codefactor.io/repository/github/Stephen-RA-King/{{ cookiecutter.pkg_name }}
[codeql-image]: https://github.com/Stephen-RA-King/{{ cookiecutter.pkg_name }}/actions/workflows/codeql-analysis.yml/badge.svg
[codeql-url]: https://github.com/Stephen-RA-King/{{ cookiecutter.pkg_name }}/actions/workflows/codeql-analysis.yml
{% if cookiecutter.use_commitizen == 'y' -%}
[commitizen-image]: https://img.shields.io/badge/commitizen-friendly-brightgreen.svg
[commitizen-url]: http://commitizen.github.io/cz-cli/
{%- endif %}
[conventional-commits-image]: https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg?style=flat-square
[conventional-commits-url]: https://conventionalcommits.org
[deepsource-image]: https://static.deepsource.io/deepsource-badge-light-mini.svg
[deepsource-url]: https://deepsource.io/gh/Stephen-RA-King/{{ cookiecutter.pkg_name }}/?ref=repository-badge
[downloads-image]: https://static.pepy.tech/personalized-badge/{{cookiecutter.pkg_name}}?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads
[downloads-url]: https://pepy.tech/project/{{cookiecutter.pkg_name}}
[format-image]: https://img.shields.io/pypi/format/{{ cookiecutter.pkg_name }}
{% if cookiecutter.use_isort == 'y' -%}
[isort-image]: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
[isort-url]: https://github.com/pycqa/isort/
{%- endif %}
[lgtm-alerts-image]: https://img.shields.io/lgtm/alerts/g/Stephen-RA-King/wymple17.svg?logo=lgtm&logoWidth=18
[lgtm-alerts-url]: https://lgtm.com/projects/g/Stephen-RA-King/wymple17/alerts/
[lgtm-quality-image]: https://img.shields.io/lgtm/grade/python/g/Stephen-RA-King/wymple17.svg?logo=lgtm&logoWidth=18
[lgtm-quality-url]: https://lgtm.com/projects/g/Stephen-RA-King/wymple17/context:python
[license-image]: https://img.shields.io/pypi/l/{{cookiecutter.pkg_name}}
[license-url]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.pkg_name }}/blob/main/license
{% if cookiecutter.use_mypy == 'y' -%}
[mypy-image]: http://www.mypy-lang.org/static/mypy_badge.svg
[mypy-url]: http://mypy-lang.org/
{%- endif %}
{% if cookiecutter.use_pre_commit == 'y' -%}
[pre-commit-image]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit-url]: https://github.com/pre-commit/pre-commit
[pre-commit.ci-image]: https://results.pre-commit.ci/badge/github/Stephen-RA-King/gitwatch/main.svg
[pre-commit.ci-url]: https://results.pre-commit.ci/latest/github/Stephen-RA-King/gitwatch/main
{%- endif %}
[pypi-url]: https://pypi.org/project/{{ cookiecutter.pkg_name }}/
[pypi-image]: https://img.shields.io/pypi/v/{{cookiecutter.pkg_name}}.svg
[python-version-image]: https://img.shields.io/pypi/pyversions/{{cookiecutter.pkg_name}}
[readthedocs-image]: https://readthedocs.org/projects/{{ cookiecutter.pkg_name }}/badge/?version=latest
[readthedocs-url]: https://{{ cookiecutter.pkg_name }}.readthedocs.io/en/latest/?badge=latest
[requirements-status-image]: https://requires.io/github/Stephen-RA-King/{{ cookiecutter.pkg_name }}/requirements.svg?branch=main
[requirements-status-url]: https://requires.io/github/Stephen-RA-King/{{ cookiecutter.pkg_name }}/requirements/?branch=main
[status-image]: https://img.shields.io/pypi/status/{{cookiecutter.pkg_name}}.svg
[tests-image]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.pkg_name}}/actions/workflows/tests.yml/badge.svg
[tests-url]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.pkg_name}}/actions/workflows/tests.yml
[wiki]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.pkg_name }}/wiki

