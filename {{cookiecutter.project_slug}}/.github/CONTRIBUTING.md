Thank you for considering improving {{ cookiecutter.pkg_name }}, any contribution is most welcome!

# Requesting a new feature

If you would like to suggest a new feature, you can create a [feature request](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.pkg_name }}/issues/new?&template=feature_request.md).

# Reporting a bug

If you encountered an unexpected behavior, please [open a new issue](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.pkg_name }}/issues/new)
and describe the problem you have found.

An ideal bug report includes:

-   The Python version you are using.
-   The {{ cookiecutter.pkg_name }} version you are using (you can find it with `{{ cookiecutter.pkg_name }} --version`)
-   Your operating system name and version.
-   Your development environment and local setup (IDE, Terminal, project context, any relevant information that could be useful).
-   Some [minimal reproducible example](https://stackoverflow.com/help/mcve).

# Implementing changes

If you want to enhance {{ cookiecutter.pkg_name }} by implementing a changes, please [open a new issue](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.pkg_name }}/issues/new) first.


Then, implement the following workflow:

1.  Fork the [{{ cookiecutter.pkg_name }}](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.pkg_name }}) project from GitHub.

2. Create a virtual environment with your favourite tool (virtualenv with virtualenv wrapper, venv etc)
using one of the supported versions of Python: ![](https://img.shields.io/pypi/pyversions/{{ cookiecutter.pkg_name }}).

3. Activate your virtual environment.

4. Clone the repository locally:

        $ git clone git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.pkg_name }}.git
        $ cd {{ cookiecutter.pkg_name }}

5. Install {{ cookiecutter.pkg_name }} in development mode:

        $ pip install -e .

6. Install pre-commit hooks that will check your commits:

        $ pre-commit install --install-hooks

7. Create a new branch from `{{ cookiecutter.initial_git_branch_name }}`:

        $ git checkout {{ cookiecutter.initial_git_branch_name }}
        $ git branch fix_bug
        $ git checkout fix_bug

8. Implement the modifications. During the process of development, honor [PEP 8](https://www.python.org/dev/peps/pep-0008/) as much as possible.

9. Add unit tests and ensure all are passing:

        $ tox

10. Update the documentation.

11. If your development modifies {{ cookiecutter.pkg_name }} behavior, update the `CHANGELOG.md` file with your changes.

12. `add` and `commit` your changes, then `push` your local project:

        $ git add .
        $ git commit -m 'Add succinct explanation of what changed'
        $ git push origin fix_bug

13. If previous step failed due to the pre-commit hooks, fix reported errors and try again.

14. Finally, [open a pull request]({{ cookiecutter.github_username }}/{{ cookiecutter.pkg_name }}/compare) before getting it merged!
