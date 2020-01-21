FROM python:3.5-alpine

ARG USER_ID=1000
ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  HOME=/home/django

RUN apk --no-cache add \
    bash \
    build-base \
    curl \
    gcc \
    gettext \
    git \
    libffi-dev \
    linux-headers \
    openssl \
    musl-dev \
    postgresql-dev \
    tini \
    zlib-dev \
    jpeg-dev \
    && pip install "poetry==1.0.2"

WORKDIR /pysetup
COPY ./server/poetry.lock ./server/pyproject.toml /pysetup/

RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

WORKDIR /code
COPY ./server /code

RUN addgroup --system --gid $USER_ID django \
    && adduser --system --home $HOME --uid $USER_ID --ingroup django django

RUN chown -R django /code $HOME
USER django

ENTRYPOINT ["/sbin/tini", "--"]
CMD ["gunicorn", "wsgi:application", "-b", "0.0.0.0:8000"]
