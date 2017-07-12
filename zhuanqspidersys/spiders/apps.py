from django.apps import AppConfig


class SpidersConfig(AppConfig):
    name = 'spiders'

    def ready(self):
        from spiders.models import Work, Author, Style
