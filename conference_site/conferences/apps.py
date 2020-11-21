from django.apps import AppConfig

class ConferencesConfig(AppConfig):
    name = 'conferences'

    def ready(self):
        import conferences.signals
