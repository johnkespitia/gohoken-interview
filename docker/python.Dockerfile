# set base image (host OS)
FROM python:3.11

# set the working directory in the container
WORKDIR /src

# install poetry
RUN pip install poetry
RUN pip install redis
RUN pip install coverage
RUN pip install httpx


# copy the pyproject.toml and poetry.lock to the working directory
COPY ./backend/pyproject.toml ./backend/poetry.lock ./

# install project dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# copy the dependencies file to the working directory
COPY ./backend/app/ .

# Expose the port on which your application runs
EXPOSE 8000

# command to run on container start
CMD ["make", "run"]