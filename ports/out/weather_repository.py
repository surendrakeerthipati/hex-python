from abc import ABC, abstractmethod


class BaseRepository(ABC):
    @abstractmethod
    def save_weather_info(self, weather_data: dict[str, str]) -> None:
        pass
