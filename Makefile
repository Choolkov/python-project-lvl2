build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

rebuild:
	make build
	python3 -m pip uninstall -y hexlet-code
	make package-install

lint:
	poetry run flake8 gendiff

install:
	poetry install

poetry-install:
	curl -sSL https://install.python-poetry.org | python3 -
