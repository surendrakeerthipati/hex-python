from typing import Optional

from ports.out.weather_repository import BaseRepository
from ports.out.weather_service import BaseWeatherService


class DomainManager:
    def __init__(
        self,
        weather_service: Optional[BaseWeatherService] = None,
        weather_repo: Optional[BaseRepository] = None,
    ) -> None:
        self.weather_service = weather_service
        self.weather_repo = weather_repo
        pass

    def get_weather_data(self, state_cd: str) -> dict:
        assert self.weather_service is not None
        return self.weather_service.get_weather_info(state_cd=state_cd)

    def save_weather_info(self, data: dict[str, str]) -> dict:
        assert self.weather_repo is not None
        return self.weather_repo.save_weather_info(data)
