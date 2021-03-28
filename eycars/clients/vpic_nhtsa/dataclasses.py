from typing import Any

from dataclasses import dataclass


@dataclass
class BaseResponse:
    Count: int
    Message: str
    SearchCriteria: str
    Results: list[Any]


@dataclass
class CarModel:
    Make_ID: int
    Make_Name: str
    Model_ID: 1861
    Model_Name: str


@dataclass
class ModelsForMakeResponse(BaseResponse):
    Results: list[CarModel]
