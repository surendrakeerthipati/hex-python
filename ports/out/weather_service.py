from abc import ABC, abstractmethod


class BaseWeatherService(ABC):
    @abstractmethod
    def get_weather_info(self, state_cd: str) -> dict:
        pass
