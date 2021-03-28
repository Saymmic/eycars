from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from eycars.cars.api.views import CarViewSet
from eycars.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet, basename="users")
router.register(r"cars", CarViewSet, basename="cars")


app_name = "api"
urlpatterns = router.urls
