

from typing import Optional

from ports.out.http_interface import BaseHttpService




class DomainManager:

    def __init__(self, weather_service: Optional[BaseHttpService] = None) -> None:
        self.weather_service = weather_service
        pass

    def get_weather_data(self,today_date:str) -> dict:
        assert self.weather_service is not None
        return self.weather_service.get_weather_info(today_date=today_date)