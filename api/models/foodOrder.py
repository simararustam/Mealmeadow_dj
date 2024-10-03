from django.db import models
from .order import Order
from .food import Food

class OrderFood(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, default=None)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{Food.name} x {self.quantity}"
