from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from eycars.cars.managers import CarModelManager
from eycars.users.models import User
from eycars.utils.models import BaseModel


class Make(BaseModel):
    external_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=512)

    def __str__(self) -> str:
        return f"{self.external_id} {self.name}"


class CarModel(BaseModel):
    external_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=1024)

    make = models.ForeignKey(Make, on_delete=models.CASCADE, related_name="car_models")
    ratings = models.ManyToManyField(
        User, through="Rating", through_fields=("car_model", "user"), related_name="car_ratings"
    )

    objects = CarModelManager()

    def __str__(self) -> str:
        return f"{self.external_id} {self.name}"


class Rating(BaseModel):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "car_model")

    def __str__(self) -> str:
        return f"{self.user} {self.car_model} : {self.rating}"
