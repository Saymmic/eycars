from django.apps import AppConfig


class CarsConfig(AppConfig):
    name = 'cars'

    def ready(self):
        try:
            import eycars.cars.signals  # noqa F401
        except ImportError:
            pass
