FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements.txt .

EXPOSE 8002:80

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]