from django.contrib import admin

from eycars.cars.models import CarModel, Make, Rating


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ("external_id", "name", "make")
    ordering = ("created",)


@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ("external_id", "name")
    ordering = ("created",)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("rating", "car_model", "user")
    ordering = ("created",)
