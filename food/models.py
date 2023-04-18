from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class FoodItem(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=255)
    item_desc = models.CharField(max_length=255)
    item_price = models.DecimalField(max_digits=5, decimal_places=2)
    item_image = models.CharField(max_length=1024, default="https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg")

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse('food:detail', kwargs={'pk': self.pk})
