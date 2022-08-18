from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.utilities.data_classes import EventBridgeEvent

from adapters.out.weather_ddb_service import WeatherDdbService
from domain.hex_manager import DomainManager

tracer = Tracer()
logger = Logger(child=True)


domain_mgr = None  # declared as global vars - for init purposes


def event_handler(event: EventBridgeEvent):
    print("Entered into Event Handler ::")
    global domain_mgr
    if domain_mgr is None:
        domain_mgr = DomainManager(weather_repo=WeatherDdbService.from_env())
    if event.detail_type == "Weather Alert":
        domain_mgr.save_weather_info(event.detail)
    else:
        logger.warn(
            f"Unknown Event Received, Implement an handler for detail-type {event.detail_type}"
        )
