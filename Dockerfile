FROM python:3.9.6-slim-buster
RUN apt-get update && apt-get upgrade -y
RUN apt-get install git curl python3-pip ffmpeg -y
RUN python3.9 -m pip install -U pip
COPY . /apphttps://heroku.com/deploy?template=https://github.com/QueenArzoo/VCPlayBot
WORKDIR /app https://heroku.com/deploy?template=https://github.com/QueenArzoo/VCPlayBot
RUN python3.9 -m pip install -U -r requirements.txt
CMD python3.9 -m VCPlayBot deploy

