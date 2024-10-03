from django.db import models
from django.utils import timezone

class Notification(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, default=None)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, default=None)
    message = models.CharField(max_length=255)
    type = models.CharField(max_length=50, default='default_value')  # Order or General
    created_at = models.DateTimeField(default=timezone.now)

    
    def check_notifications(self):
        # Logic to check notifications
        pass
