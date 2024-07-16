install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd