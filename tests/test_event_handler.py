from dataclasses import dataclass

import pytest
from aws_lambda_powertools.utilities.data_classes import EventBridgeEvent
from pytest_mock import MockerFixture

import app_events as handler
from adapters.out.weather_ddb_service import WeatherDdbService

from .fake_services.fake_weather_ddb_service import FakeWeatherDdbService


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


def test_event_handler(lambda_context, mocker: MockerFixture):

    event_input = {
        "version": "0",
        "id": "1a582f25-eaa6-2862-adc6-bf4014f78627",
        "detail-type": "Weather Alert",
        "source": "muthu",
        "account": "684805258957",
        "time": "2022-08-18T04:49:10Z",
        "region": "us-east-1",
        "resources": [],
        "detail": {
            "stateCd": "CA",
            "onset": "2022-08-17T14:00:00-07:00",
            "expires": "2022-08-18T08:00:00-07:00",
            "ends": "2022-08-18T08:00:00-07:00",
            "status": "Actual",
            "messageType": "Alert",
            "category": "Met",
            "severity": "Severe",
            "certainty": "Likely",
            "urgency": "Expected",
            "event": "Red Flag Warning",
            "sender": "w-nws.webmaster@noaa.gov",
            "senderName": "NWS Reno NV",
        },
    }
    storage = FakeWeatherDdbService("fake")
    mocker.patch.object(WeatherDdbService, "from_env", return_value=storage)
    handler_resposne = handler.lambda_handler(
        EventBridgeEvent(event_input), lambda_context
    )
    assert handler_resposne is None
