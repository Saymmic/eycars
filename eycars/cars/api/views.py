from typing import Optional

from django.db.models import Avg, Count
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from eycars.cars.api.serializers import CarModelSerializer, RatingSerializer
from eycars.cars.models import CarModel


class CarViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = CarModel.objects.select_related("make")
    serializer_class = CarModelSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(average_rating=Avg("rating__rating"))
        return queryset

    @action(detail=True, methods=["post"])
    def rate(self, request: Request, pk: Optional[int] = None) -> Response:
        car_model = self.get_object().pk
        user = self.request.user.pk

        data = {**request.data, "user": user, "car_model": car_model}

        serializer = RatingSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False)
    def popular(self, request):
        queryset = self.get_queryset().annotate(number_of_ratings=Count("ratings")).order_by("-number_of_ratings")

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
