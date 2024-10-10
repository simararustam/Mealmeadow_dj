from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, default=None)
    # food_items = models.ManyToManyField('Food')
    status = models.CharField(max_length=20,
                              choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')])
    order_date = models.DateTimeField(default=timezone.now)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def calculate_total_amount(self):
        total = sum(item.food.price * item.quantity for item in self.order_items.all())
        self.total_amount = total
        self.save()

    def __str__(self):
        return f"Order {self.id} from {self.restaurant.name}"