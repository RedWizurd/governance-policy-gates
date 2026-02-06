PYTHON ?= python3
VENV ?= .venv
PIP := $(VENV)/bin/pip
PY := $(VENV)/bin/python

.PHONY: setup check run

setup:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

check:
	test -f memory_policy.json || cp memory_policy.example.json memory_policy.json
	test -f approval_policy.json || cp approval_policy.example.json approval_policy.json
	test -f risk_policy.json || cp risk_policy.example.json risk_policy.json
	$(PY) validate_policies.py

run:
	$(PY) agent.py --mode builder --operation read --approve-risky=false
