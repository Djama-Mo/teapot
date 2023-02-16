FROM tiangolo/uwsgi-nginx:python3.8-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app

RUN pip3 install --upgrade pip -r requirements.txt

ENV STATIC_URL /static
ENV STATIC_PATH /app/static

ENV FLASK_DEBUG development

EXPOSE 5000