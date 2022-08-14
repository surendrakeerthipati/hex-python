from aws_lambda_powertools import Tracer, Logger
from aws_lambda_powertools.event_handler.api_gateway import Router
from adapters.out.weather_rest_service import WeatherInfoRestService

from domain.hex_manager import DomainManager

tracer = Tracer()
logger = Logger(child=True)

router = Router()

domain_mgr = None  # declared as global vars - for init purposes


@router.get("/weather-info")
@tracer.capture_method
def get_weather_data():
    print("Entered into routes controller ::")
    global domain_mgr
    if domain_mgr is None:
        domain_mgr = DomainManager(weather_service=WeatherInfoRestService.from_env())
    query_params = router.current_event.query_string_parameters
    date = query_params.get("todaysDate")
    res = domain_mgr.get_weather_data(today_date=date)
    return {"payload": res}
