from django.apps import AppConfig


class CollapsewebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CollapseWeb'
    
    def ready(self):
        import CollapseWeb.signals