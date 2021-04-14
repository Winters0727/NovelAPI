from django.urls import path

# from rest_framework import routers

from .views import BookListView, BookDetailView, ChapterListView, ChapterDetailView, CommentListView, CommentDeleteView, ReviewListView, ReviewDetailView

app_name = 'book'

urlpatterns = [
    path('book/', BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('chapter/', ChapterListView.as_view(), name='chapter-list'),
    path('chapter/<int:index>/', ChapterDetailView.as_view(), name='chapter-detail'),
    path('comment/', CommentListView.as_view(), name='comment-list'),
    path('comment/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    path('review/', ReviewListView.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail')
]