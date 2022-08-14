from aws_lambda_powertools import Tracer
from aws_lambda_powertools.event_handler.api_gateway import Router
from adapters.out.weather_rest_service import WeatherInfoRestService

from domain.hex_manager import DomainManager

tracer = Tracer()
router = Router()


domain_manager = DomainManager(weather_service=WeatherInfoRestService.from_env())


@router.get("/weather-info")
@tracer.capture_method
def get_weather_data():
    print("Entered into routes controller ::")
    query_params = router.current_event.query_string_parameters
    date = query_params.get("todaysDate")
    res = domain_manager.get_weather_data(today_date=date)
    return {"payload": res}
