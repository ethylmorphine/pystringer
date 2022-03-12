.PHONY: clean deploy

PWD=$(shell pwd)
HOST_PYTHON=$(shell which python3)
RM=$(shell which rm)
LS=$(shell which ls)
CD=$(shell which cd)

VENV=$(PWD)/.venv
VENV_PYTHON=$(VENV)/bin/python3
VENV_PIP=$(VENV)/bin/pip3
VENV_UWSGI=$(VENV)/bin/uwsgi
REQUIREMENTS=$(PWD)/requirements.txt
SRC=$(PWD)/src

$(VENV):
	$(HOST_PYTHON) -m venv $(VENV)
	$(VENV_PYTHON) -m pip install -U pip
	$(LS) -l $(VENV)

init: $(VENV)
	$(VENV_PIP) install -r $(REQUIREMENTS)

deploy:
	$(VENV_UWSGI) -s 0.0.0.0:8888 --enable-threads --manage-script-name --chdir $(SRC) --mount /=main:app

clean:
	[ ! -d $(VENV) ] || $(RM) -rf -- $(VENV)
	[ ! -d $(SRC)/__pycache__ ] || $(RM) -rf -- $(SRC)/__pycache__
