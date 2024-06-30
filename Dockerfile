ARG PYTHON_VERSION=3.12

FROM python:${PYTHON_VERSION}-slim AS base

ARG ADMIN_USERNAME
ARG ADMIN_PASSWORD
ARG ADMIN_EMAIL

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

RUN adduser --disabled-password --gecos "" --shell "/sbin/nologin" --uid "10001" collapse

USER collapse

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

COPY --chown=collapse:collapse . /app

RUN ./migrate.sh

ENV DJANGO_SUPERUSER_USERNAME=${ADMIN_USERNAME}
ENV DJANGO_SUPERUSER_PASSWORD=${ADMIN_PASSWORD}
ENV DJANGO_SUPERUSER_EMAIL=${ADMIN_EMAIL}

RUN python manage.py createsuperuser --noinput

CMD ["python", "manage.py", "runserver", "--insecure", "0.0.0.0:8000"]
