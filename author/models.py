import os

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    def __str__(self):
        return f'{self.nickname}'

    def profile_path(self, filename):
        return os.path.join('profile', f'{self.nickname}{os.path.splitext(filename)[1]}')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to=profile_path)