FROM python:3.8.10-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

WORKDIR /app/orderFlow

ENTRYPOINT python manage.py migrate && python manage.py makemigrations && python3 manage.py runserver 0.0.0.0:5000

