upload:
	rm dist/*
	python3 setup.py sdist
	twine upload dist/* -r pypi