from django.contrib import admin

from .models import Book, Chapter, ChapterComment, Review, ReviewComment

# Register your models here.
admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(ChapterComment)
admin.site.register(Review)
admin.site.register(ReviewComment)