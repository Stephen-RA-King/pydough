## 1.2.2 (2023-04-11)

### Refactor

- **tasks.py**: remove commented code
- **{{-cookiecutter.pkg_name-}}.py**: escape main() from mypy check
- **post_installation.py**: replace hard coded description text
- **development.in**: remove eradicate as not flake8v6 compatible
- add raise(SystemError(main)) idiom
- **tasks**: remove unused f string
- update pre-commit versions
- correct logger message string
- migrate deprecated importlib.resources functions

### Fix

- **post_gen_project**: wrong variable name used for resource files
- fix: lazy logging format use %s no f strings
- exclude config test if no config files selected
- jinja template - replace pgk with project

### Feat

- add support for pickle serialization

## 1.2.1 (2022-08-01)

### Refactor

- **changelog.md**: remove markdown

### Fix

- **__init__.py**: log file path fully relative

## 1.2.0 (2022-08-01)

### Feat

- bump version after new feature
- Add provision for example scripts

### Fix

- **setup.cfg**: error in script entry point

## 1.1.1 (2022-07-21)

### Fix

- **setup.cfg**: entry point for cli script

## 1.1.0 (2022-07-21)

### Fix

- template git branch name
- add config command to readthedocs.yml
- **code**: incorrect markdown

## v1.0.0 (2022-05-06)
