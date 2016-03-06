PROJECT_NAME = righter
PROJECT_HOME = "."
PROJECT_CODE = $(PROJECT_HOME)/src
PROJECT_TEST = $(PROJECT_HOME)/tests
NEW_PYTHONPATH = $(PROJECT_CODE):$(PYTHONPATH)

.PHONY: tests


clean:
	@echo "Cleaning up *.pyc, *.sw[a-z] and *~ files"
	@find . -name "*.pyc" -delete
	@find . -name "*.sw[a-z]" -delete
	@find . -name "*~" -delete

setup:
	@echo "Installing dependencies..."
	@pip3 install -r $(PROJECT_HOME)/requirements.txt

pep8:
	@echo "Checking source-code PEP8 compliance"
	@-pep8 $(PROJECT_CODE)

pep8_tests:
	@echo "Checking tests code PEP8 compliance"
	@-pep8 $(PROJECT_TEST)

lint:
	@echo "Running pylint"
	@pylint $(PROJECT_CODE)/$(PROJECT_NAME)

style: pep8 pep8_tests lint

tests:
	@echo "Running unit and integration and acceptance tests..."
	@nosetests -s  --cover-branches --cover-erase --with-coverage --cover-inclusive --cover-package=$(PROJECT_NAME) --tests=$(PROJECT_TEST) --with-xunit

run:
	@PYTHONPATH=$(NEW_PYTHONPATH) python -m $(PROJECT_NAME).main
