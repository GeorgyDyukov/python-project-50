install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

update:
	pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff_package

selfcheck:
	poetry check

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff_package --cov-report xml

check: selfcheck test lint
