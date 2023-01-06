FROM python:3.7

WORKDIR /usr/src/app
COPY app/ .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./hangman.py" ]