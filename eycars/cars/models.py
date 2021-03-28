from django.db import models

from eycars.utils.models import BaseModel


class Make(BaseModel):
    external_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=512)


class CarModel(BaseModel):
    external_id = models.IntegerField(unique=True)
    make = models.ForeignKey(Make, on_delete=models.CASCADE, related_name="car_models")
    name = models.CharField(max_length=1024)
