import logging

logger = logging.getLogger('API_TEST')


def assert_status_code(response, expected_status_code=200):
    try:
        assert response.status_code == expected_status_code, f"Failure: Expected status code {expected_status_code}, but received {response.status_code}"
        logger.info(f"Success: Status code is {response.status_code} as expected.")
    except AssertionError as e:
        logger.error(str(e))

        raise


def assert_response_keys(response_data, expected_keys):
    response_keys = response_data.keys()
    try:
        for key in expected_keys:
            assert key in response_keys, f"Failure: Expected key '{key}' not found in response."
        logger.info(f"Success: All expected keys {expected_keys} found in response.")
    except AssertionError as e:
        logger.error(str(e))
        raise


def assert_response_body(response, expected_response):
    actual_response = response.json()
    try:
        assert actual_response == expected_response, f"Failure: Expected response body {expected_response}, got {actual_response}"
        logger.info(f"Success: Response body matches expected response.")
    except AssertionError as e:
        logger.error(str(e))
        raise
