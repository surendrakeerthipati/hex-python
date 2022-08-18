from typing import Optional

import requests

from ports.out.weather_service import BaseWeatherService


class FakeWeatherInfoRestService(BaseWeatherService):
    def __init__(self, session: Optional[requests.Session] = None) -> None:
        self.session = session

    @classmethod
    def from_env(cls) -> "FakeWeatherInfoRestService":
        session = requests.Session()
        return cls(session=session)

    def get_weather_info(self, state_cd: str) -> dict:
        assert self.session is not None
        params = {"area": state_cd}
        response = {'success':'True'}        
        return response
