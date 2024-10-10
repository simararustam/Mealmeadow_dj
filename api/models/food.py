from django.db import models
from .restaurant import Restaurant

class Food(models.Model):
    name = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='foods', default=None)
    food_type = models.CharField(max_length=50)
    price = models.FloatField()
    discounted_price = models.FloatField(blank=True, null=True)
    discounted_rate = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)
    mehsul_muddeti = models.CharField(max_length=100, blank=True)
    elan_muddeti = models.CharField(max_length=100, blank=True)
    quantity = models.IntegerField(default=0)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.food_type,
            'price': self.price,
            'discounted_price': self.discounted_price,
            'discounted_rate': self.discounted_rate,
            'description': self.description,
            'mehsul_muddeti': self.mehsul_muddeti,
            'elan_muddeti': self.elan_muddeti,
            'restaurant_name': self.restaurant.name,
            'image': self.image.url if self.image else None, 
        }
