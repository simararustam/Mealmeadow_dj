from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
 
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, default=None)
    food_items = models.ManyToManyField('Food')
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')])
    order_date = models.DateTimeField(default=timezone.now)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # def save(self, *args, **kwargs):
    #     self.total_amount = sum(food.price for food in self.food_items.all())
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} from {self.restaurant.name}"
