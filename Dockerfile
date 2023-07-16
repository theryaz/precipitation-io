FROM python:3.12.0b4-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install build-essential python3-smbus python3-rpi.gpio -y

RUN pip install quart

COPY . .

CMD [ "/usr/local/bin/python app.py"]