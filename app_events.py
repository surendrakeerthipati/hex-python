from aws_lambda_powertools import Logger, Tracer
import os
from aws_lambda_powertools.utilities.data_classes import event_source, EventBridgeEvent
from aws_lambda_powertools.logging import correlation_paths
from adapters.eventbridge_adapter import event_handler

os.environ["POWERTOOLS_SERVICE_NAME"] = "hex-event-handler"

tracer = Tracer()
logger = Logger()


@logger.inject_lambda_context(correlation_id_path=correlation_paths.EVENT_BRIDGE)
@tracer.capture_lambda_handler
@event_source(data_class=EventBridgeEvent)
def lambda_handler(event: EventBridgeEvent, context):
    logger.info(f"Received {event.detail_type} with detail {event.detail}")
    event_handler(event=event)
