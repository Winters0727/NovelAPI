import os

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    def __str__(self):
        return f'{self.title} by {self.author}'

    def cover_path(self, filename):
        return os.path.join('cover', f'{self.title}-cover{os.path.splitext(filename)[1]}')

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    cover = models.ImageField(upload_to=cover_path)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated_at']

class Chapter(models.Model):
    def __str__(self):
        return f'{self.book.title} Chapter {self.index}'
        
    index = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField()