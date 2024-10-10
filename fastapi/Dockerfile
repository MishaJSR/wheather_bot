FROM python:3.11-slim
WORKDIR /usr/src/app/fast
COPY . .
RUN poetry update
RUN poetry install
ENV PYTHONUNBUFFERED=1