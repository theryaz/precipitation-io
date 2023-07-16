FROM python:3.10-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install build-essential python-dev -y

RUN pip install quart RPi.GPIO smbus

COPY . .

CMD [ "/bin/bash python /app/app.py"]