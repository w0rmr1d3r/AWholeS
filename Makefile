install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

freeze:
	CUSTOM_COMPILE_COMMAND="make freeze" pip-compile --no-emit-index-url -v -o requirements.txt pyproject.toml
	CUSTOM_COMPILE_COMMAND="make freeze-dev" pip-compile --extra "dev" --no-emit-index-url -v -o requirements-dev.txt pyproject.toml

freeze-upgrade:
	CUSTOM_COMPILE_COMMAND="make freeze" pip-compile --upgrade --no-emit-index-url -v -o requirements.txt pyproject.toml
	CUSTOM_COMPILE_COMMAND="make freeze-dev" pip-compile --extra "dev" --upgrade --no-emit-index-url -v -o requirements-dev.txt pyproject.toml

format:
	black .

lint:
	black --check .

.PHONY: install install-dev freeze freeze-upgrade format lint
