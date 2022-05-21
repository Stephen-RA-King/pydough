# {{ cookiecutter.pkg_name }}
> Short blurb about what your product does.



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
{% if cookiecutter.license == 'MIT' -%}
[![licence: mit][mit-license-image]][mit-license-url]
{%- endif %}
{% if cookiecutter.license == "BSD" -%}
[![licence: bsd][bsd-license-image]][bsd-license-url]
{%- endif %}
{% if cookiecutter.license == "GPL-3.0" -%}
[![licence: gplv3][gplv3-license-image]][gplv3-license-url]
{%- endif %}
{% if cookiecutter.license == "Apache-2.0" -%}
[![licence: apachev2][apachev2-license-image]][apachev2-license-url]
{%- endif %}


One to two paragraph statement about your product and what it does.

![](assets/header.png)
![](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/raw/main/assets/header.png)

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
[**Read the Docs**](https://{{ cookiecutter.pkg_name }}.readthedocs.io/en/latest/?)


## Meta
{% if cookiecutter.github_username == 'Stephen-RA-King' -%}
[![](assets/linkedin.png)](https://linkedin.com/in/stephen-k-3a4644210)
[![](assets/github.png)](https://github.com/Stephen-RA-King/Stephen-RA-King)
[![](assets/www.png)](https://www.Stephen-RA-King)
[![](assets/email.png)](mailto:stephen.ra.king@gmail.com)
{% endif %}

{{cookiecutter.author_name}} : {{cookiecutter.email}}

Distributed under the {{cookiecutter.license}} License. See `LICENSE` for more information.

[https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.pkg_name }}](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.pkg_name }})



<!-- Markdown link & img dfn's -->
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
{% if cookiecutter.license == 'MIT' -%}
[mit-license-image]: https://img.shields.io/badge/license-MIT-blue
[mit-license-url]: https://choosealicense.com/licenses/mit/
{%- endif %}
{% if cookiecutter.license == "BSD" -%}
[bsd-license-image]: https://img.shields.io/badge/license-BSD-blue
[bsd-license-url]: https://www.openbsd.org/policy.html
{%- endif %}
{% if cookiecutter.license == "GPL-3.0" -%}
[gplv3-license-image]: https://img.shields.io/badge/license-GPLv3-blue
[gplv3-license-url]: https://choosealicense.com/licenses/gpl-3.0/
{%- endif %}
{% if cookiecutter.license == "Apache-2.0" -%}
[apachev2-license-image]: https://img.shields.io/badge/license-Apache%202-blue.svg
[apachev2-license-url]: https://choosealicense.com/licenses/apache-2.0/
{%- endif %}
[wiki]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.pkg_name }}/wiki
