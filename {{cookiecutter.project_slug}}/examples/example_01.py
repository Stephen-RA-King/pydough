"""Example script 01 - Demonstrate usage of package features."""

# First party modules
from {{cookiecutter.pkg_name}} import {{cookiecutter.pkg_name}}

num, result = {{cookiecutter.pkg_name}}.get_config()
exp_result = [True for i in range(num)]
print(f"Result from function 'get_config': {result}")


result = {{ cookiecutter.pkg_name }}.fizzbuzz(16)
print(f"Result from function 'fizzbuzz(16)': {result}")


result = {{ cookiecutter.pkg_name }}.fibonacci(10)
print(f"Result from function 'fibonacci(10)': {result}")

