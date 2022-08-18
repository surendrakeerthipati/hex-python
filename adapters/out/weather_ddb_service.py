from __future__ import annotations

from typing import TYPE_CHECKING, Optional
import os
import boto3
from ports.out.weather_repository import BaseRepository
if TYPE_CHECKING:
    from mypy_boto3_dynamodb.service_resource import Table
from datetime import datetime


class WeatherDdbService(BaseRepository):
    def __init__(self, table: Optional[Table] = None) -> None:
        self.table = table

    @classmethod
    def from_env(cls) -> "WeatherDdbService":
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table(os.environ["TABLE_NAME"])
        return cls(table=table)

    def save_weather_info(self, data: dict[str, str]) -> None:
        assert self.table is not None
        self.table.put_item(Item={"pk": data["stateCd"], "sk": str(datetime.now()), **data})
        pass
