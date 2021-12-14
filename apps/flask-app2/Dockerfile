FROM python:3.8.10-alpine3.13
ENV FLASK_ENV development
RUN pip install Flask
COPY ./app /flask-app
WORKDIR /flask-app
ENTRYPOINT ["/usr/local/bin/flask", "run", "-h", "0.0.0.0"]