from django.db import models
# from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)
    address = models.TextField() #--migrate ele
    rating = models.FloatField(blank=True, null=True)
    # owner = models.OneToOneField(User, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=255, default='Default')
    contact_number = models.CharField(max_length=20, blank=True, default='')
    email = models.EmailField(default='default@example.com')
    logo = models.CharField(max_length=255, blank=True, null=True)
    # logo = models.ImageField(upload_to='restaurant_logos/')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'rating': self.rating,
            'owner_name': self.owner_name,
            'contact_number': self.contact_number,
            'email': self.email,
            'logo': self.logo
        }