SRC_DIR = offline-semester-downloader


init: 
	pip install -r requirements.txt

test: 
	pytest

check: 
	pycodestyle $(SRC_DIR)/*.py
	pylint --persistent=n -E -s n **/*.py

debug: 
	pylint -r y --persistent=n

clean: 
	rm -rv .pytest_cache/
	rm -rv $(SRC_DIR)/__pycache__/

.PHONY : init test check debug clean
