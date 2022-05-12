FROM python:3.9-alpine
WORKDIR /apps/{{ cookiecutter.project_slug }}/
COPY src/{{ cookiecutter.project_slug }}/. .
COPY requirements/development.txt .
RUN ["pip", "install", "-r", "development.txt"]
CMD ["python", "{{ cookiecutter.project_slug }}.py"]
