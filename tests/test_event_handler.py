import app_event_handler as handler
from tests.test_app_api_poc import lambda_context
from aws_lambda_powertools.utilities.data_classes import EventBridgeEvent


def test_event_handler(lambda_context):
    event_input = {
        "version": "0",
        "id": "0d079340-135a-c8c6-95c2-41fb8f496c53",
        "detail-type": "Send-Email",
        "source": "triggered this event_handler from ...",
        "account": "poc-testing",
        "time": "2022-02-01T18:41:53Z",
        "region": "us-east-1",
        "detail": {"data": "success"},
    }
    handler_resposne = handler.lambda_handler(
        EventBridgeEvent(event_input), lambda_context
    )
    assert handler_resposne is None
