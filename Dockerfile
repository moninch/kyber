FROM python:3.10

mkdir /app

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["unicorn", "main:app", "--bind", "0.0.0.0:8000" , "--log-level", "debug"]