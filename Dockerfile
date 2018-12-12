FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y zsh git wget python-pip python-dev build-essential software-properties-common
#oh-my-zsh, because how do we live without it?
RUN git clone https://github.com/robbyrussell/oh-my-zsh.git

ADD ./app /app


ADD ./app/configs/.zshrc /root/.zshrc
RUN git clone https://github.com/robbyrussell/oh-my-zsh.git
ADD ./app/configs/lovelace.zsh-theme /oh-my-zsh/themes/lovelace.zsh-theme

WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5001:5001
ENTRYPOINT ["python"]
CMD ["server.py"]
