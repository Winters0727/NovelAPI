from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

from book.models import Book

# Create your models here.
class Review(models.Model):
    def __str__(self):
        return f'{self.author} : {self.title}'
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    context = models.TextField()
    view_count = models.IntegerField(default=0, blank=True)
    review_point = models.IntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(10)])

class ReviewComment(models.Model):
    def __str__(self):
        return f'{self.author} : {self.context}'

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    context = models.CharField(max_length=100, blank=False)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

class TemporaryReview(models.Model):
    def __str__(self):
        return f'{self.author} : {self.title}'
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    context = models.TextField()
    review_point = models.IntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(10)])