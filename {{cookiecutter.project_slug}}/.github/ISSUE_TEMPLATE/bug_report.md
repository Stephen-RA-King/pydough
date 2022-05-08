---
name: Bug report
about: Create a report to help us improve Black's quality
title: ""
labels: "T: bug"
assignees: ""
---

<!--
Please make sure that the bug is not already fixed either in newer versions or the
current development version. To confirm this, you have two options:

1. Update {{ cookiecutter.project_name }} version if a newer release exists: `pip install -U {{ cookiecutter.project_name }}`
2. Or run _{{ cookiecutter.project_name }}_ on your machine:
   - create a new virtualenv (make sure it's the same Python version);
   - clone this repository;
   - run `pip install -e .[d]`;
   - run `pip install -r requirements.txt`
   - make sure it's sane by running `python -m pytest`; and
   - run `{{ cookiecutter.project_name }}` like you did last time.
-->

**Describe the bug**

<!-- A clear and concise description of what the bug is. -->

**To Reproduce**

<!--
Minimal steps to reproduce the behavior with source code and {{ cookiecutter.project_name }}'s configuration.
-->

For example, take this code:

```python
...
```

And run it with these arguments:

```sh
$ 
```

The resulting error is:

>  ...

**Expected behavior**

<!-- A clear and concise description of what you expected to happen. -->

**Environment**

<!-- Please complete the following information: -->

- {{ cookiecutter.project_name }}'s version: <!-- e.g. [main] -->
- OS and Python version: <!-- e.g. [Linux/Python 3.7.4rc1] -->

**Additional context**

<!-- Add any other context about the problem here. -->
