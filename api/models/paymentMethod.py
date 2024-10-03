from django.db import models
from django.contrib.auth.models import User

class PaymentMethod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    card_number = models.CharField(max_length=16)
    expiration_date = models.CharField(max_length=5)  # MM/YY format
    cardholder_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Payment Method for {self.user.username}"