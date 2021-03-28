from __future__ import annotations

from typing import TYPE_CHECKING

from django.db import models
from eycars.clients.vpic_nhtsa.dataclasses import CarModel as CarModelDataclass

if TYPE_CHECKING:
    from eycars.cars.models import CarModel


class CarModelManager(models.Manager):
    def get_or_create_from_datacalss(self, model: CarModelDataclass) -> tuple[CarModel, bool]:
        from eycars.cars.models import Make

        make, _ = Make.objects.get_or_create(name=model.Make_Name, external_id=model.Make_ID)
        car_model, created = self.get_or_create(name=model.Model_Name, external_id=model.Model_ID, make=make)

        return car_model, created
