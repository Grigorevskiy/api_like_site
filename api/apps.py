
from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'api_like.api'

    def ready(self):
        pass


class ApiConfig(AppConfig):
    name = 'api'
    verbose_name = "Управление контентом"

    def ready(self):
        import api.signals.signals
