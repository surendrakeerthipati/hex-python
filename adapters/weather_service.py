from typing import Optional

import requests
from ports.out.http_interface import BaseHttpService


class WeatherInfoService(BaseHttpService):
    def __init__(self, session: Optional[requests.Session] = None) -> None:
        # super().__init__()
        self.session = session

    @classmethod
    def from_env(cls) -> "WeatherInfoService":
        session = requests.Session()
        return cls(session=session)

    def get_weather_info(self, today_date: str) -> dict:
        assert self.session is not None
        params = {"apikey": "dummy"}
        response = self.session.get(
            "https://dataservice.accuweather.com/currentconditions/v1/topcities/10",
            params=params,
        )
        if response.status_code == 401:
            return {"status": "UnAuthorized"}
        print(f"loggers printed ::{response} ")
        return response
