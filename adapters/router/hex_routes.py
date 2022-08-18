from aws_lambda_powertools import Tracer, Logger
from aws_lambda_powertools.event_handler.api_gateway import Router
from adapters.out.weather_rest_service import WeatherInfoRestService
from aws_lambda_powertools.event_handler.exceptions import (
    BadRequestError,
)

from domain.hex_manager import DomainManager

tracer = Tracer()
logger = Logger(child=True)

router = Router()

domain_mgr = None  # declared as global vars - for init purposes


@router.get("/weather-info")
@tracer.capture_method
def get_weather_data():
    logger.info("Entered into routes controller ::")
    global domain_mgr
    if domain_mgr is None:
        domain_mgr = DomainManager(weather_service=WeatherInfoRestService.from_env())
    query_params = router.current_event.query_string_parameters
    if query_params is None or "stateCd" not in query_params:
        raise BadRequestError("Missing required parameter - 'stateCd'")
    state = query_params.get("stateCd")
    res = domain_mgr.get_weather_data(state_cd=state)
    return {"payload": res}
