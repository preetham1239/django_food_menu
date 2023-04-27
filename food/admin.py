from django.contrib import admin
# Register your models here.
from .models import FoodItem


"""
This class is used to configure the admin interface.
But why? Because the admin interface is a Django app. So? Because Django apps are reusable apps that can be used in multiple projects.
So, why is the admin interface in a separate folder and configured here? 
"""
admin.site.register(FoodItem)