build-HexApiFunction:
	poetry build	
	poetry run pip install --upgrade -t $(ARTIFACTS_DIR) dist/*.whl