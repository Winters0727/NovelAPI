import os

from django.db import models
from django.conf import settings

# Create your models here.

class Book(models.Model):
    def __str__(self):
        return f'{self.title} by {self.author}'

    def cover_path(self, filename):
        return os.path.join('cover', f'{self.title}-cover{os.path.splitext(filename)[1]}')

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    cover = models.ImageField(upload_to=cover_path, default=os.path.join('cover', 'default.png'))
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated_at']

class Chapter(models.Model):
    def __str__(self):
        return f'{self.book.title} Chapter {self.index}'
        
    index = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField()

class Comment(models.Model):
    def __str__(self):
        return f'{self.author} : {self.context}'

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    context = models.CharField(max_length=100, blank=False)
    parent_comment = models.ForeignKey('self', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

class Review(models.Model):
    def __str__(self):
        return f'{self.author} : {self.title}'
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    context = models.TextField()
    review_point = models.IntegerField(default=5)