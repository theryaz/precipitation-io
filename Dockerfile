FROM python:3.12.0b4-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install build-essential -y

RUN pip install quart

RUN pip install rpi-gpio \
 && pip install smbus

COPY . .

CMD [ "/usr/local/bin/python /app/app.py"]