FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements.txt .

EXPOSE 8000:8000

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
