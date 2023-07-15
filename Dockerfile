FROM arm32v7/python:3.11-alpine

WORKDIR /app

COPY . .
COPY .venv .venv

RUN ls -la

ENTRYPOINT [ "python", "rain_barrels/app.py"]