from django.apps import AppConfig


class FoodConfig(AppConfig):
    """
    This class is used to configure the food app.
    Because the food app is a Django app. Django apps are reusable apps that can be used in multiple projects.
    That is the reason why the food app is in a separate folder and configured here.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'food'
