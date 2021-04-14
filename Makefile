setup:
	python -m venv ~/.devops-project

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=mylib --cov=hello test_hello.py

lint:
	pylint --disable=R,C,E1120 hello.py mylib/*.py
	
format:
	black *.py mylib/*.py

all: install lint test