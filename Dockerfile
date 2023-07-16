FROM python:3.10-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install build-essential -y

RUN pip install poetry

COPY . .

RUN poetry install

CMD [ "/bin/bash python /app/app.py"]