from django.apps import AppConfig


class TodoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ToDoApp'
    def ready(self):
        import ToDoApp.signals

        from . import openai_api
        openai_api.start()





