from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    food_type = models.CharField(max_length=50)
    price = models.FloatField()
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, related_name='foods')
    discounted_price = models.FloatField(blank=True, null=True)
    discounted_rate = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True)
    image_url = models.CharField(max_length=255, blank=True)
    pickup_time = models.CharField(max_length=100, blank=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.food_type,
            'price': self.price,
            'discounted_price': self.discounted_price,
            'discounted_rate': self.discounted_rate,
            'description': self.description,
            'image_url': self.image_url,
            'pickup_time': self.pickup_time,
            'restaurant_id': self.restaurant.id,
            'restaurant_name': self.restaurant.name
        }
