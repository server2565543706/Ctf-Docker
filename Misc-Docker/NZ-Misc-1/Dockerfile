FROM python:3.9

WORKDIR /usr/src/app

COPY game.py .
COPY flag.py .



EXPOSE 80

CMD while true; do python ./game.py; sleep 600; done
