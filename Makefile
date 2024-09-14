make setup:
	pip3 install -r requirements.txt

make lint:
	pylint main.py

make test:
	pytest