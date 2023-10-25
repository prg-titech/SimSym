.PHONY: shell
shell:
	@pipenv shell

.PHONY: lint
lint:
	@flake8 -- .
	@mypy .

.PHONY: format
format:
	@isort .
	@autopep8 -ir .
