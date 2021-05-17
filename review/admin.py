from django.contrib import admin

from .models import Review, ReviewComment, TemporaryReview
# Register your models here.

admin.site.register(Review)
admin.site.register(ReviewComment)
admin.site.register(TemporaryReview)