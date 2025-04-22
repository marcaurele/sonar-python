FROM ghcr.io/astral-sh/uv:0.6.10 AS uv

###############
# Build stage #
###############
# Put here any build steps in order to not install building tools into the final image
FROM python:3.12.10-alpine3.21 AS builder


ENV PYTHONUNBUFFERED=1 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8 \
    UV_SYSTEM_PYTHON=true

EXPOSE 5000
    
COPY --from=uv /uv /bin/

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-editable

RUN set -ex \
    && adduser -D app

WORKDIR /app/src

COPY main.py /app/src/

ENV PATH="/app/.venv/bin:$PATH"

USER app

CMD ["flask", "--app", "main", "run", "--host", "0.0.0.0"]