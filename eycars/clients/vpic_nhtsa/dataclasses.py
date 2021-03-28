from typing import Any

from dataclasses import dataclass


@dataclass(frozen=True)
class BaseResponse:
    Count: int
    Message: str
    SearchCriteria: str
    Results: list[Any]


@dataclass(frozen=True)
class CarModel:
    Make_ID: int
    Make_Name: str
    Model_ID: 1861
    Model_Name: str


@dataclass(frozen=True)
class ModelsForMakeResponse(BaseResponse):
    Results: list[CarModel]
