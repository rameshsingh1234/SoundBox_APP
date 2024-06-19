import os
import logging
import pytest
import json
from Reusable.api_requests import make_request
from Reusable.assertion import assert_status_code, assert_response_keys, assert_response_body
from Utilities import CustomLogger
from Utilities.readproperties import ReadConfig

# Get the log directory and CSV file path from the configuration
log_directory = ReadConfig.get_logs_directory()
log_file_path = os.path.join(log_directory, "test.log")

# Set up the logger
logger = CustomLogger.setup_logger('API_TEST', log_file_path, level=logging.DEBUG)

# Get the CSV file path from the configuration
csv_file_path = ReadConfig.get_csv_file_path()

# Read the CSV data
csv_data = ReadConfig.read_csv(csv_file_path)

# Extract test case IDs for custom test names
test_params = [pytest.param(data, id=data['Testcase ID']) for data in csv_data]


@pytest.mark.parametrize("test_data", test_params)
def test_api(test_data):
    url = test_data['url']
    method = test_data['method']
    headers = json.loads(test_data['headers']) if test_data['headers'] else {}
    payload = json.loads(test_data['payload']) if test_data['payload'] else {}
    expected_status_code = int(test_data['expected_status_code'])
    expected_keys = test_data['expected_response_keys'].split(',') if test_data['expected_response_keys'] else None
    expected_response = json.loads(test_data['expected_responce_body']) if test_data['expected_responce_body'] else None

    logger.info("***********************API Test Start *****************************")
    logger.info("***********************API Request Made *****************************")
    response = make_request(url, method, headers, payload)

    # Check if the response content type is JSON
    if 'application/json' in response.headers.get('Content-Type', ''):
        response_data = response.json()
        logger.info("*********************** Response Received *****************************")
    else:
        response_data = None
        logger.info("*********************** Response is not in JSON format *****************************")
        logger.info(response.text)

    assert_status_code(response, expected_status_code)
    logger.info("*********************** Status Code Asserted *****************************")

    if expected_keys and response_data:
        assert_response_keys(response_data, expected_keys)
        logger.info("***********************Response Keys Asserted*****************************")

    if expected_response and response_data:
        assert_response_body(response, expected_response)
        logger.info("***********************Response Body Asserted*****************************")

    logger.info("***********************API Test Ends*****************************")
