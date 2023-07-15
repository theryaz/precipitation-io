FROM python:3.11-alpine

WORKDIR /app

COPY . .

ENTRYPOINT [ "python", "rain_barrels/app.py"]