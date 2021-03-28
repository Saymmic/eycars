from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from eycars.cars.models import CarModel, Rating
from eycars.clients.vpic_nhtsa.clients import client as vpic_client


class CarModelSerializer(serializers.ModelSerializer):
    make = serializers.CharField(source="make.name")
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = CarModel
        fields = ["uuid", "name", "make", "average_rating"]

    def validate(self, attrs: dict) -> dict:
        attrs = super().validate(attrs)
        make_name = attrs["make"]["name"]
        model_name = attrs["name"]

        if not vpic_client.models_for_make.get(make=make_name, model=model_name):
            raise ValidationError(f"Model name {model_name} of make {make_name} not found.")

        return attrs

    def create(self, validated_data: dict) -> CarModel:
        model = vpic_client.models_for_make.get(make=validated_data["make"]["name"], model=validated_data["name"])

        car_model, _ = CarModel.objects.get_or_create_from_datacalss(model=model)
        return car_model


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ["rating", "user", "car_model"]
        extra_kwargs = {"user": {"write_only": True}, "car_model": {"write_only": True}}
