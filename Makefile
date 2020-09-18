SHELL := /bin/bash

PYTEST_FLAGS=--show-capture=no --cov-config=tests/.coveragerc --cov=app --cov-report term --cov-report html

.PHONY: $(SERVICES) logs

FORCE: ;  ## always run targets with this keyword


## NOTE: Add this to your .bashrc to enable make target tab completion
##    complete -W "\`grep -oE '^[a-zA-Z0-9_.-]+:([^=]|$)' ?akefile | sed 's/[^a-zA-Z0-9_.-]*$//'\`" make
## Reference: https://stackoverflow.com/a/38415982

help: ## This info
	@echo '_________________'
	@echo '| Make targets: |'
	@echo '-----------------'
	@echo
	@cat Makefile | grep -E '^[a-zA-Z\/_-]+:.*?## .*$$' | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo

run_passing_tests:
	python tests/ping_api.py

run_failing_tests:
	python tests/bad_api.py

email_commit:
	python notification.py
