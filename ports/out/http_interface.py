from abc import ABC, abstractmethod


class BaseHttpService(ABC):
    @abstractmethod
    def get_weather_info(self, today_date: str) -> dict:
        pass
