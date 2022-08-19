import os

from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.data_classes import (EventBridgeEvent,
                                                          event_source)

from adapters.out.weather_ddb_service import WeatherDdbService
from domain.hex_manager import DomainManager

os.environ["POWERTOOLS_SERVICE_NAME"] = "hex-event-handler"

tracer = Tracer()
logger = Logger()


domain_mgr = None  # declared as global vars - for init purposes


@logger.inject_lambda_context(correlation_id_path=correlation_paths.EVENT_BRIDGE)
@tracer.capture_lambda_handler
@event_source(data_class=EventBridgeEvent)
def lambda_handler(event: EventBridgeEvent, context):
    logger.info(f"Received {event.detail_type} with detail {event.detail}")
    global domain_mgr
    if domain_mgr is None:
        domain_mgr = DomainManager(weather_repo=WeatherDdbService.from_env())
    if event.detail_type == "Weather Alert":
        domain_mgr.save_weather_info(event.detail)
    else:
        logger.warn(
            f"Unknown Event Received, Implement an handler for detail-type {event.detail_type}"
        )