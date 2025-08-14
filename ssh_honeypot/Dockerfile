FROM ubuntu:latest

WORKDIR /ws

COPY . /ws
EXPOSE 22

RUN apt update -y && apt install ssh -y
CMD [ "/bin/bash" ]
