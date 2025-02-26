# Dockerfile
FROM python:3.8-slim

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "data_collection/collect_data.py"]
