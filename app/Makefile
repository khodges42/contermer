.PHONY: install start

install:
	pip install -r requirements.txt; \
	cp ./configs/.zshrc /root/.zshrc; \
	git clone https://github.com/robbyrussell/oh-my-zsh.git /oh-my-zsh/ ;\
    cp ./configs/lovelace.zsh-theme /oh-my-zsh/themes/lovelace.zsh-theme

start:
	python server.py