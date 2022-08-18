from typing import Optional

import requests

from ports.out.weather_service import BaseWeatherService


class WeatherInfoRestService(BaseWeatherService):
    def __init__(self, session: Optional[requests.Session] = None) -> None:
        self.session = session

    @classmethod
    def from_env(cls) -> "WeatherInfoRestService":
        session = requests.Session()
        return cls(session=session)

    def get_weather_info(self, state_cd: str) -> dict:
        assert self.session is not None
        params = {"area": state_cd}
        response = self.session.get(
            "https://api.weather.gov/alerts/active",
            params=params,
        )
        if response.status_code == 401:
            return {"status": "UnAuthorized"}
        print(f"loggers printed :: {response.json()} ")
        return response.json()
