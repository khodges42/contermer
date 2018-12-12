FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y zsh git wget python-pip python-dev build-essential software-properties-common

ADD ./app /app

WORKDIR /app
EXPOSE 5001:5001
RUN make install
ENTRYPOINT ["make"]
CMD ["start"]
