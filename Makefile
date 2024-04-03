#!make
# include .env
export

.PHONY: curl-old curl install dev

install:
	pip install pipenv
	pipenv install
	pipenv run python challenge/manage.py migrate
	pipenv run python challenge/manage.py loaddata challenge/api/fixtures/data.json
	

dev:
	pipenv run python challenge/manage.py runserver

curl-old:
	curl --data '@./challenge/api/fixtures/batiments.json'  -H "Content-Type: application/json"  http://127.0.0.1:8000/api/sum/  

curl:
	curl -H "Content-Type: application/json"  http://127.0.0.1:8000/api/sum/?bat_id=1  
