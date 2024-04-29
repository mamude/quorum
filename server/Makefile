VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
ISORT = $(VENV)/bin/isort

clean:	
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "venv" -type d | xargs rm -rf	

build-env:
	python3 -m pip install --upgrade pip
	python3 -m venv $(VENV)

install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) app/main.py

isort:
	$(ISORT) .


