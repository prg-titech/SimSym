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

help: ## ヘルプを表示する
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
