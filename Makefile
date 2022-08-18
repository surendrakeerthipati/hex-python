build-HexApiFunction:
	poetry build	
	poetry run pip install --upgrade -t $(ARTIFACTS_DIR) dist/*.whl
build-HexEventHandler:
	poetry build	
	poetry run pip install --upgrade -t $(ARTIFACTS_DIR) dist/*.whl