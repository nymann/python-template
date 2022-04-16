ensure-test-dependencies:
	command -v pytest 2>/dev/null || make install-tests

test: unit-tests integration-tests

unit-tests: ${VERSION} ensure-test-dependencies
	pytest tests/unit_tests

integration-tests: ${VERSION} ensure-test-dependencies
	pytest tests/integration_tests
