from django.db import models
from .restaurant import Restaurant

class Setting(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=None)
    logo = models.ImageField(upload_to='settings_logos/', blank=True, null=True)
    owner_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()

    def update_settings(self, new_data):
        if 'logo' in new_data:
            self.logo = new_data['logo']
        if 'owner_name' in new_data:
            self.owner_name = new_data['owner_name']
        if 'contact_number' in new_data:
            self.contact_number = new_data['contact_number']
        if 'email' in new_data:
            self.email = new_data['email']
        self.save()

    def __str__(self):
        return f"Settings for {self.restaurant.name}"
