# Use UV's Python image as builder
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

WORKDIR /app

# Enable bytecode compilation and copy mode
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# Install dependencies
COPY pyproject.toml ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install --system -r pyproject.toml

# Copy and install source code
COPY . /app/

# Final stage
FROM python:3.12-slim-bookworm

WORKDIR /app

# Copy installed packages and source code
COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /app/server.py /app/server.py

CMD ["python", "server.py"] 