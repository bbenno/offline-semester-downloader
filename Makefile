SRC_DIR = offline-semester-downloader
DOC_DIR = docs

init: 
	pip3 install -r requirements.txt

test: clean
	pytest --random-order

tidy: clean
	@echo "\nTidying code with black..."
	black -l 79 offline-semester-downloader
	black -l 79 tests
	black -l 79 setup.py

check: clean tidy
	pycodestyle $(SRC_DIR)/*.py
	pylint --persistent=n -E -s n **/*.py

debug: 
	pylint -r y --persistent=n

clean: 
	rm -r .pytest_cache
	find . | grep -E "(__pycache__)" | xargs rm -r

.PHONY: init test check debug clean
