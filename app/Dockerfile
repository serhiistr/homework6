FROM python:3.10

COPY app.py /app/app.py

RUN apt-get update -y && apt install -y iputils-ping

WORKDIR /app

CMD ["python", "app.py"]