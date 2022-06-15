# Cookiecutter Python Development template

_**A general purpose development template for the creation of a Python application, library or package**_


![](https://github.com/Stephen-RA-King/cc_template/raw/main/header.png)


## Template Features

All the following features are optional:

* [**Flake8**][flake8-url] - Tool that glues together pycodestyle, pyflakes & mccabe
* [**Black**][black-url] - Code formatter
* [**MyPy**][mypy-url] - Tool for static type checking
* [**Pre-Commit**][pre-commit-url] - A framework for managing pre-commit hooks (pre-configured with many hooks)
* [**isort**][isort-url] - Sort imports automatically
* [**Bandit**][bandit-url] -  Finds common security issues 
* [**Sphinx**][sphinx-url] -  Package for creating documentation
* [**Click**][click-url] -  Package for creating Command line interfaces
* [**Invoke**][invoke-url] - Common package maintenance tasks are automated with this python library

The following tool is mandatory (you will thank me later):
* [**pip-tools**][pip-tools-url] -  Pins every single package dependency (even the dependency’s dependencies)


### Other Features
* Automatically installs pre-commit (if selected) and associated git hook
* Automatically configures git message template
* Selection of licenses to choose from
* Optionally include [**Safety**][safety-url] to check dependencies for known security vulnerabilities
* Optionally include [**Flakeheaven**][flakeheaven-url] Flake8 wrapper to replace flakehell
* Optionally include version control and release with [**python-semantic-release**](https://github.com/relekang/python-semantic-release) or [**bump2version**][bump2version-url] 
* Options to specify Docstring style (Google, Numpy, Sphinx or [**PEP257**][pep257-url])
* Optionally include [**Commitizen**][commitizen-url] for parsing and enforcing descriptive git commits
* Optionally include Logging using the dictConfig() configuration
* Automatically include badges based on your selections e.g.:

[![pre-commit][pre-commit-image]][pre-commit-url]
[![Imports: isort][isort-image]][isort-url]
[![Code style: black][black-image]][black-url]
[![Checked with mypy][mypy-image]][mypy-url]
[![security: bandit][bandit-image]][bandit-url]

## Pre Installation Requirements

1. Python 3.8, 3.9 or 3.10
2. git
3. Virtual Environment. (I like [**virtualenv**][virtualenv-url] with [**virtualenv_wrapper**][virtualenvwrapper-url]. I love "workon".)
4. [**Cookiecutter**][cookiecutter-url] installed into the Virtual Environment

## Installation

Assuming you are at the command prompt of the activated virtual environment
simply type the following:

```bash
$ cookiecutter https://github.com/stephen-ra-king/cc_template
```

cookiecutter will prompt you for a selection of inputs and eventually [**pip-tools**][pip-tools-url] will
pin your dependencies from the inputs you have given.
This template uses [**layered requirements**][layered-url] (the default being "development")
so now install the packages using pip as follows:

```bash
$ pip install -r <package-name>/requirements.txt
```

## Optional Post-Installation steps
### Recommended Post Installation Requirements:
You will need accounts with the following services:
- [GitHub](http://github.com) - Login and Generate your token
- [Read the Docs](https://readthedocs.org/)
- [TestPyPi](https://test.pypi.org/) - Login and Generate your token
- [PyPi](https://pypi.org/) - Login and Generate your token
- [Codecov.io](https://about.codecov.io/)


### Finalization Steps

1. Put your pypi and testpypi keys into the .pypirc file
2. Create a remote repository using GitHub
3. If using GitHub actions - Add your PyPi and TestPyPi tokens to the repository actions secrets with the following variable names:
- TEST_PYPI_API_TOKEN
- PYPI_API_TOKEN
4. If you are using Python Semantic Release, create the following environment variables:
- GH_TOKEN = _GitHub token_
- REPOSITORY_PASSWORD = _PyPI token_
- REPOSITORY_USERNAME = \__token__
5. Import the GitHub repository into [**Read the Docs**](https://readthedocs.org/)
6. Install your package as an "editable" package.

Editable installs were not possible until 2021, but that has been remedied by [**PEP660**][pep660-url].
This can be performed by either 'pip' or 'setuptools'
```sh
$ python -m pip install -e . 
```
```sh
$ python setup.py develop
```
7. Push the local files to GitHub

Note Git is automatically initialized and the following is automatically run by the post install hook
```sh
$ git remote add origin git@github.com:<user>/<repository-name>.git 
```
So simply add, commit and push
```sh
$ git add *
$ git commit -m "chore: initial commit"
$ git push -u origin main 
```
Note: If you chose to use the [**Pre-Commit**][pre-commit-url] package then many hooks (e.g. Flake8, Black, Bandit Prettier etc.)
will now download and configure themselves and eventually be run against each file in the repository.
This may take some time and some files may get modified. You will need to "git add" these files again.

8. Again when the time comes create a git tag (optionally signed) and push to the remote
```sh
$ git tag -s 0.1.0 -m "chore: 0.1.0 tag"
$ git push --tags
```

9. Create build artefacts with the following command:
```sh
$ python -m build
```
10. Now upload the build artefacts to the test repository for final testing:
```sh
$ python -m twine upload --config-file .pypirc -r testpypi dist/*
```

11. When the time comes, release to the main repository:
```sh
$ python -m twine upload --config-file .pypirc dist/*
```

12. If you are using services requires.io, codecov.io, codefactor.io
and deepsource.io then you will need to login to those services with your GitHub account and import your respositories

## Note
Some badges can take up to 24 Hrs to update (yes download badge ... I am looking at you). So please be patient.





### Using Python Semantic Release (PSR)
If you opted to use PSR then the future uploading to GitHub & uploading to PyPI, 
will be done automatically.
After you have committed changes to git, issue the following command:
```sh
$ semantic-release publish
```
Publish will do a sequence of things:

- Update changelog file.
- Run semantic-release version.
- Push changes to git.
- Run build_command and upload the distribution file to your repository.
- Run semantic-release changelog and post to your vcs provider.
- Attach the files created by build_command to GitHub releases.

### Documentation creation
"Read the docs" will automatically generate new documentation when you push to GitHub.
Howver you can manually generate local documenattion by simply moving to the "docs" directory and issuing the make command.
```sh
$ make html
```
You can then open the "...docs/_build/html/index.html" file with a browser.
It is generally best to clear the _build directory when generating new documentation by using the following command
```sh
$ make clean html
```



## Known Issues
### 1 - Python semantic Release (PSR) v7.28.1 on Windows
PSR will not find a .pypirc file because the Path command is linux style
 

Workaround:
  
in file ...\Lib\site-packages\semantic_release\repository.py
change line 84 from:
```python
elif not Path("~/.pypirc").expanduser().exists():
```
to
```python
elif not Path(".pypirc").expanduser().exists():
```

### 2 - Manually update .github workflows: 'tests.yml' & 'codeql-analysis.yml'
GitHub Actions use a templating format - probably Jinja2 which is what cookiecutter uses.
For this reason I have had to exclude the workflow files from cookiecutter.
If cookiecutter came across any variables that it was unaware of it would throw an exception.  
Therefore the following variables need to be changed to whatever you are using:  
- default-branch1  
- default-branch2  
- package_name


## Finally
Now develop! ... Go away now.



## Meta
[![](assets/linkedin.png)](https://linkedin.com/in/stephen-k-3a4644210){:target="_blank" rel="noopener"}
[![](assets/github.png)](https://github.com/Stephen-RA-King/Stephen-RA-King)
[![](assets/www.png)](https://www.Stephen-RA-King)
[![](assets/email.png)](mailto:stephen.ra.king@gmail.com) 


Author: Stephen RA King

Distributed under the MIT License. See ``LICENSE`` for more information.

_For more examples and usage, please refer to the [Wiki][wiki]._



<!-- Markdown link & img dfn's -->
[invoke-url]: https://www.pyinvoke.org/
[virtualenv-url]: https://virtualenv.pypa.io
[virtualenvwrapper-url]: https://pypi.org/project/virtualenvwrapper/
[cookiecutter-url]: https://github.com/cookiecutter/cookiecutter
[layered-url]: https://github.com/jazzband/pip-tools/#workflow-for-layered-requirements
[flake8-url]: https://github.com/PyCQA/flake8
[sphinx-url]: https://github.com/sphinx-doc/sphinx
[click-url]: https://github.com/pallets/click/
[commitizen-url]: https://github.com/commitizen-tools/commitizen
[safety-url]: https://github.com/pyupio/safety
[pep257-url]: https://peps.python.org/pep-0257/
[pep660-url]: https://peps.python.org/pep-0660/

[google-docstring-url]: https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings
[numpy-docstring-utl]: https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard



[bump2version-url]: https://github.com/c4urself/bump2version
[pip-tools-url]: https://github.com/jazzband/pip-tools/
[flakeheaven-url]: https://github.com/flakeheaven/flakeheaven

[pre-commit-image]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit-url]: https://github.com/pre-commit/pre-commit

[isort-image]: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
[isort-url]: https://github.com/PyCQA/isort

[black-image]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-url]: https://github.com/psf/black

[bandit-image]: https://img.shields.io/badge/security-bandit-yellow.svg
[bandit-url]: https://github.com/PyCQA/bandit

[mypy-image]: http://www.mypy-lang.org/static/mypy_badge.svg
[mypy-url]: https://github.com/python/mypy

[mit-license-image]: https://img.shields.io/badge/license-MIT-blue
[mit-license-url]: https://choosealicense.com/licenses/mit/
[bsd-license-image]: https://img.shields.io/badge/license-BSD-blue
[bsd-license-url]: https://www.openbsd.org/policy.html
[gplv3-license-image]: https://img.shields.io/badge/license-GPLv3-blue
[gplv3-license-url]: https://choosealicense.com/licenses/gpl-3.0/
[apachev2-license-image]: https://img.shields.io/badge/license-Apache%202-blue.svg
[apachev2-license-url]: https://choosealicense.com/licenses/apache-2.0/

[wiki]: https://github.com/stephen-ra-king/cc_template/wiki
[github]: https://github.com/stephen-ra-king/cc_template
