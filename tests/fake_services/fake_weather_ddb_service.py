from __future__ import annotations

from typing import TYPE_CHECKING, Optional
import os
import boto3
from ports.out.weather_repository import BaseRepository

if TYPE_CHECKING:
    from mypy_boto3_dynamodb.service_resource import Table


class FakeWeatherDdbService(BaseRepository):
    def __init__(self, table: Optional[Table] = None) -> None:
        self.table = table

    @classmethod
    def from_env(cls) -> "FakeWeatherDdbService":
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table(os.environ["TABLE_NAME"])
        return cls(table=table)

    # dummy method for handling dynamo saves
    def save_weather_info(self, data: dict[str, str]) -> None:
        assert self.table is not None
        # saving to dynamo db goes here,
        return "Saved"
