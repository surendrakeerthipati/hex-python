from dataclasses import dataclass

import app_hex_api
import pytest


@pytest.fixture
def lambda_context():
    @dataclass
    class LambdaContext:
        function_name: str = "test"
        memory_limit_in_mb: int = 128
        invoked_function_arn: str = (
            "arn:aws:lambda:eu-west-1:123456789012:function:test"
        )
        aws_request_id: str = "da658bd3-2d6f-4e7b-8ec2-937234644fdc"

    return LambdaContext()


def test_api_call_success(lambda_context):
    minimal_event = {
        "path": "/weather-info",
        "queryStringParameters": {"stateCd": "CA"},
        "httpMethod": "GET",
        "requestContext": {
            "requestId": "227b78aa-779d-47d4-a48e-ce62120393b8"
        },  # correlation ID
    }

    response = app_hex_api.lambda_handler(minimal_event, lambda_context)
    assert response["statusCode"] == 200
    assert response["body"] != ""


def test_api_call_failure(lambda_context):
    minimal_event = {
        "path": "/weather-info",
        "queryStringParameters": {"stateCd_invalid": ""},
        "httpMethod": "GET",
        "requestContext": {
            "requestId": "227b78aa-779d-47d4-a48e-ce62120393b8"
        },  # correlation ID
    }

    message_info = (
        '{"statusCode":400,"message":"Missing required parameter - \'stateCd\'"}'
    )

    ret = app_hex_api.lambda_handler(minimal_event, lambda_context)
    assert ret["statusCode"] == 400
    assert ret["body"] == message_info
