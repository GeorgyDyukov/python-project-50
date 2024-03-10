build:
	poetry build

publish:
	poetry publish --dry-run

update:
    pip install --user dist/*.whl --force-reinstall
