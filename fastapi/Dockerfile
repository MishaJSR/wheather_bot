FROM python:3.11-slim
WORKDIR /usr/src/app/fast
COPY . .
RUN pip install poetry
RUN poetry install --no-root --only main
ENV PYTHONUNBUFFERED=1
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000