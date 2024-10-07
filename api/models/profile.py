from django.db import models
# from django.contrib.auth.models import User
from users.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profili"
    