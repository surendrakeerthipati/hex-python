from abc import ABC, abstractmethod


class BaseWeatherService(ABC):
    @abstractmethod
    def get_weather_info(self, today_date: str) -> dict:
        pass
