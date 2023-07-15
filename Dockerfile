FROM arm32v7/python:3.11-alpine

WORKDIR /app

RUN pip install poetry
RUN poetry config virtualenvs.in-project true
COPY . .
RUN poetry install

ENTRYPOINT [ "python", "rain_barrels/app.py"]