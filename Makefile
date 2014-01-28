clean:
	@find . -name "*.pyc" -delete

deps:
	@python setup.py install

test, t: clean
	@python tests/manage.py test app

sub:
	@sublime .

help, h:
	@grep '^[^#[:space:]].*:' Makefile | awk -F ":" '{print $$1}'
