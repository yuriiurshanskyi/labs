.DEFAULT_GOAL := all

all: install test run deploy

install:
	echo "Installing packages..."
	pip3 install pipenv
	pipenv --python 3.9
	pipenv install requests
	pipenv install ntplib
	pipenv install pytest

test:
	echo "Testing..."
	pipenv run pytest tests/tests.py >> results.txt

run:
	echo "Running code..."
	pipenv run python3.9 app.py >> results.txt

deploy:
	echo "Deploy on GitHub"
	git add results.txt
	git commit -m "lab2: results.txt"
	git push origin main lab2/
