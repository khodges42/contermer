FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y zsh git wget python-pip python-dev build-essential software-properties-common

ADD ./app /app

WORKDIR /app
EXPOSE 5001:5001
<<<<<<< HEAD
RUN make install
ENTRYPOINT ["make"]
CMD ["start"]
=======
ENTRYPOINT ["python"]
CMD ["server.py"]
>>>>>>> 7ff551fdc439bc1a869152d27400a5caf3c3e83a
