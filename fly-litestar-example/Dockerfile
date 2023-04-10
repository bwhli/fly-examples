FROM python:3.11-buster as venv

ENV POETRY_VERSION=1.4.1
RUN curl -sSL https://install.python-poetry.org | python

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN python -m venv --copies /app/venv
RUN . /app/venv/bin/activate && ~/.local/share/pypoetry/venv/bin/poetry install --no-root

FROM python:3.11-slim-buster as prod

COPY --from=venv /app/venv /app/venv/
ENV PATH /app/venv/bin:$PATH

WORKDIR /app
COPY ./fly_litestar_example /app/fly_litestar_example

# Start application
CMD ["uvicorn", "fly_litestar_example.app.main:app", "--host", "0.0.0.0", "--port", "8080"]