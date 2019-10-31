init:
	pip install -r requirements.txt

test:
	tox

.PHONY: init test