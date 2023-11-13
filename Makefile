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

.PHONY: coverage
coverage: ## カバレッジのレポートを表示する
	@coverage report -m | grep -v '100%' | grep -v 'TOTAL'
	@coverage report -m | grep 'TOTAL'

.PHONY: testc
testc:	## unittest を実行し、カバレッジを表示する
	@make test
	@make coverage

.PHONY: check
check:  ## format と lint と test を全て実行する
	@make format
	@make lint
	@make test

.PHONY: checkc
checkc:  ## format と lint と test を全て実行し、カバレッジを表示する
	@make format
	@make lint
	@make test
	@make coverage

.PHONY: status-main
status-main:
	@echo "[本体]"
	@echo "ファイル数: $$(find SimSym -name '*.py' | wc -l | awk '{print $$1}')"
	@echo "総行数    : $$(find SimSym -name '*.py' | xargs wc -l | grep total | awk '{print $$1}')"
	@echo "総文字数  : $$(find SimSym -name '*.py' | xargs wc -m | grep total | awk '{print $$1}')"
	@echo "カバレッジ: $$(make coverage | grep 'TOTAL' | awk '{print $$4}')"

.PHONY: status-test
status-test:
	@echo "[テスト]"
	@echo "ファイル数: $$(find test -name '*.py' | wc -l | awk '{print $$1}')"
	@echo "総行数    : $$(find test -name '*.py' | xargs wc -l | grep total | awk '{print $$1}')"
	@echo "総文字数  : $$(find test -name '*.py' | xargs wc -m | grep total | awk '{print $$1}')"

.PHONY: status-all
status-all:
	@echo "[合計]"
	@echo "ファイル数: $$(find SimSym test -name '*.py' | wc -l | awk '{print $$1}')"
	@echo "総行数    : $$(find SimSym test -name '*.py' | xargs wc -l | grep total | awk '{print $$1}')"
	@echo "総文字数  : $$(find SimSym test -name '*.py' | xargs wc -m | grep total | awk '{print $$1}')"
	@echo "カバレッジ: $$(make coverage | grep 'TOTAL' | awk '{print $$4}')"

.PHONY: status
status: ## プロジェクトの情報を表示する
	@make status-main
	@make status-test
	@make status-all

help: ## ヘルプを表示する
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
