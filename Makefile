.PHONY: install start all

build:
	docker build -t termtainer .

start:
	docker run -p 5001:5001 -d termtainer

all: build start