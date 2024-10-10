from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class PaymentMethod(models.Model):
    # Bu modelin harda istifadəsinə baxmaq lazımdır
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    card_number = models.CharField(max_length=16)
    expiration_date = models.CharField(max_length=5)
    cardholder_name = models.CharField(max_length=100)