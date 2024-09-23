from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)
    rating = models.FloatField(blank=True, null=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'rating': self.rating
        }
