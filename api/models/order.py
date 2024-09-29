from django.db import models

class Order(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    food_items = models.ManyToManyField('Food')
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')])

    def receive_order_notification(self):
        # Logic to receive order notifications
        pass
