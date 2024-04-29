export PYTHONPATH=.
export PYTHONDONTWRITEBYTECODE=1

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
ISORT = $(VENV)/bin/isort
BLACK = $(VENV)/bin/black

clean:	
	@find . -name "__pycache__" -type d | xargs rm -rf	

build-env:
	python3 -m pip install --upgrade pip
	python3 -m venv $(VENV)

install-dev:
	$(PIP) install -r requirements.txt

install: build-env install-dev

run:	
	$(PYTHON) app/main.py

isort:
	$(ISORT) .

black:
	$(BLACK) .


