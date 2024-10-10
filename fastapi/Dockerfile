FROM python:3.10-alpine
WORKDIR /usr/src/app/fast
COPY requirements.txt /usr/src/app/fast
RUN pip install --no-cache-dir -r requirements.txt
COPY ../.. .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
EXPOSE 8000