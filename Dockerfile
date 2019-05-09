FROM python:3.7-alpine3.9

COPY . /app
WORKDIR /app

# default flask port
EXPOSE 5000

RUN pip install -r requirements.txt

CMD python server.py
#CMD tail -f /dev/null 