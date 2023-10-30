.DEFAULT_GOAL := help

.PHONY: install-dev
install-dev: ## pipenv で指定されているパッケージをインストールする (dev)
	@pipenv install --dev

.PHONY: install
install: ## pipenv で指定されているパッケージをインストールする
	@pipenv install

.PHONY: shell
shell: ## pipenv で生成された仮想環境に入る
	@pipenv shell

.PHONY: lint
lint:  ## flake8 と mypy を実行する
	@flake8 -- .
	@mypy .

.PHONY: format
format:  ## isort と autopep8 を実行する
	@isort .
	@autopep8 -ir .

.PHONY: test
test:  ## unittest を実行しカバレッジを計測する
	@coverage run -m unittest discover
	@coverage xml

.PHONY: report
report: ## カバレッジのレポートを表示する
	@coverage report -m

.PHONY: check
check:  ## format と lint と test を全て実行する
	@make format
	@make lint
	@make test

.PHONY: commit
commit:
	@make check
	@git add .
	@git commit

help: ## ヘルプを表示する
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
