FROM python:3.9

WORKDIR /usr/src/app

COPY game.py .
COPY flag.py .
COPY start.sh /usr/bin


EXPOSE 80
CMD ["/bin/bash", "-c", "/usr/bin/start.sh && while true; do python ./game.py; sleep 600; done"]

# CMD while true; do python ./game.py; sleep 600; done
