from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    address_type = models.CharField(max_length=50, choices=[('Home', 'Home'), ('Work', 'Work'), ('Other', 'Other')])
    street_address = models.CharField(max_length=255)
    # city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.address_type} address for {self.user.name} {self.user.last_name}"
    