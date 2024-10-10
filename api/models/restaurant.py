from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)
    rating = models.FloatField(blank=True, null=True)
    owner_name = models.CharField(max_length=255, default='Default')
    contact_number = models.CharField(max_length=20, blank=True, default='')
    email = models.EmailField(default='default@example.com')
    logo = models.ImageField(upload_to='restaurant_logos/', default=None)
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'rating': self.rating,
            'owner_name': self.owner_name,
            'contact_number': self.contact_number,
            'email': self.email,
            'logo': self.logo.url if self.logo else None,
        }