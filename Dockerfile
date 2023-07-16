FROM python:3.12.0b4-slim-bullseye

WORKDIR /app

RUN pip install quart
RUN pip install rpi-gpio
RUN pip install smbus

COPY . .

CMD [ "/usr/local/bin/python app.py"]