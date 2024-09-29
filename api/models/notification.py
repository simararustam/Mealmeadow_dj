from django.db import models

class Notification(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    type = models.CharField(max_length=50)  # Order or General
    timestamp = models.DateTimeField(auto_now_add=True)

    def check_notifications(self):
        # Logic to check notifications
        pass
