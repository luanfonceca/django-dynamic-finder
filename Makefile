clean:
	@find . -name "*.pyc" -delete

install:
	@python setup.py install

test: install clean
	@python tests/manage.py test app

help:
	@grep '^[^#[:space:]].*:' Makefile | awk -F ":" '{print $$1}'
