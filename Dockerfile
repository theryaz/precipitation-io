FROM python:3.10-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install build-essential -y

RUN pip install quart \
    && pip install rpi-gpio \
    && pip install smbus

COPY . .

CMD [ "/usr/local/bin/python /app/app.py"]