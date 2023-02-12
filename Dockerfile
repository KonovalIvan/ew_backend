# Use an official Python runtime as the base image
FROM python:3.8-alpine

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# Copy pyproject.toml and poetry.lock
COPY pyproject.toml poetry.lock /app/

# Install dependencies
RUN pip install poetry
RUN poetry install

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=config.settings.prod

# Run command to start the Django server
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
