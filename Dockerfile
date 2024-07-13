<<<<<<< HEAD
# Dockerfile
FROM python:3.8-slim

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "data_collection/collect_data.py"]
=======
# Dockerfile
FROM python:3.8-slim

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "data_collection/collect_data.py"]
>>>>>>> 21efe1b304df64857a2f6eefed48b3c39ac77c1c
