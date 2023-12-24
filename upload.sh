bumpversion minor
rm -rf dist/*
python3 setup.py sdist
twine upload dist/* -u __token__