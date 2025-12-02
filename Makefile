.PHONY: install test lint format

# Install dependencies
install:
	pip install -r requirements.txt

# Run tests
test:
	pytest -v

# Lint using flake8
lint:
	flake8 tests --count --max-line-length=120 --statistics

# Format code using black
format:
	black .

# Clean cache files
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
