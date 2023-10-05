FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements.txt .

EXPOSE 8000:80

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]