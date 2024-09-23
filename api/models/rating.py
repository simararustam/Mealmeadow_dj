from django.db import models

class Rating(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, related_name='ratings')
    star = models.FloatField()

    def to_dict(self):
        return {
            'id': self.id,
            'restoran_id': self.restoran.id,
            'star': self.star,
        }
