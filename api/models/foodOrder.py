from django.db import models
from .order import Order
from .food import Food

class OrderFood(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=None, related_name='order_items')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, default=None)
    food_name = food.name
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{Food.name} x {self.quantity}"
