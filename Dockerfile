FROM python:3.7

WORKDIR /usr/src/app
COPY app/ .

CMD [ "python", "./hangman.py" ]