from django.apps import AppConfig


class WesdispenserdbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wesdispenserDB'

    def ready(self) :
        import wesdispenserDB.signals 
