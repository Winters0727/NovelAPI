import os

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# from allauth.socialaccount.models import SocialAccount

from book.models import Book, Review

# Create your models here.

class Author(AbstractUser):
    def __str__(self):
        return f'{self.nickname}'

    def profile_path(self, filename):
        return os.path.join('profile', f'{self.nickname}{os.path.splitext(filename)[1]}')
    
    nickname = models.CharField(max_length=20)
    profile_image = models.ImageField(blank=True, upload_to=profile_path, default=os.path.join('profile', 'default.png'))
    followers = models.ManyToManyField('self', blank=True, related_name='followed_by')
    like_books = models.ManyToManyField(Book, blank=True, related_name='like_users')
    like_reviews = models.ManyToManyField(Review, blank=True, related_name='like_users')