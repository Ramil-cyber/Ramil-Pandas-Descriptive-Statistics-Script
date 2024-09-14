setup:
	pip3 install -r requirements.txt

lint:
	pylint main.py

test:
	pytest
