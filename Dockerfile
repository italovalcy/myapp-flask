FROM python:3.6

COPY ./requirements.txt /app/requirements.txt
COPY ./flaskr /app/flaskr

WORKDIR /app

RUN pip install -r requirements.txt
RUN rm -f requirements.txt

ENV FLASK_APP flaskr
ENV FLASK_ENV production 
RUN flask init-db

EXPOSE 8080

ENTRYPOINT flask run --host 0.0.0.0 --port 8080 --with-threads
