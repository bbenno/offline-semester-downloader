SRC_DIR = osd
DOC_DIR = docs
TST_DIR = tests

BLACK = black -l 79

init: 
	@echo "\nInstalling requirements..."
	pip3 install -r requirements.txt

test: clean
	pytest

coverage: clean
	#pytest --random-order --cov-config .coveragerc --cov-report term-missing --cov=...

flake8: 
	flake8

tidy: clean
	@echo "\nTidying code with black..."
	$(BLACK) $(SRC_DIR)
	$(BLACK) $(TST_DIR)
	$(BLACK) setup.py

check: clean tidy flake8
	pycodestyle $(SRC_DIR)/*.py
	pylint --persistent=n -E -s n **/*.py

debug: 
	pylint -r y --persistent=n

clean: 
	rm -rf .pytest_cache/
	find . | grep -E "(__pycache__)" | xargs rm -rf

.PHONY: init test check debug clean
