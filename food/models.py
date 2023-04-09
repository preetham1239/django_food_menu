from django.db import models


class FoodItem(models.Model):
    item_name = models.CharField(max_length=255)
    item_desc = models.CharField(max_length=255)
    item_price = models.DecimalField(max_digits=3, decimal_places=1)
    item_image = models.CharField(max_length=1024, default="https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg")

    def __str__(self):
        return self.item_name
