from django.apps import AppConfig


class Capp2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'capp2'

    def ready(self):
        import capp2.signals
