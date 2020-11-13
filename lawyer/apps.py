from django.apps import AppConfig


class LawyerConfig(AppConfig):
    name = 'lawyer'
    verbose_name = 'lawyer'

    def ready(self):
        from signals import auto_create_Group, auto_create_Permission
