FROM python:3.9-alpine
WORKDIR /apps/{{ cookiecutter.pkg_name }}/
COPY src/{{ cookiecutter.pkg_name }}/. .
COPY requirements/development.txt .
RUN ["pip", "install",  "--no-cache-dir", "-r", "development.txt"]
CMD ["python", "{{ cookiecutter.pkg_name }}.py"]
