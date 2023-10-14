FROM python:3.10

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV POETRY_VERSION=1.5.1

WORKDIR /app/
RUN apt-get update \
  && apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    curl \
    git \
    libpq-dev \
    wget \
  # Cleaning cache:
  && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*


# FIXME: fix downloading lib from poetry not from pip
#RUN pip install "poetry==$POETRY_VERSION"

#COPY ./poetry.lock ./pyproject.toml ./
#RUN poetry config virtualenvs.create false
#RUN poetry install

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

# Run command to start the Django server
CMD ["sh", "-c", "python manage.py runserver"]
