from django.urls import path

# from rest_framework import routers

from .views import BookListView, BookDetailView, ChapterListView, ChapterDetailView, \
ChapterCommentListView, ChapterCommentDeleteView, ReviewListView, ReviewDetailView, \
ReviewCommentListView, ReviewCommentDeleteView

app_name = 'book'

urlpatterns = [
    path('book/', BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('chapter/', ChapterListView.as_view(), name='chapter-list'),
    path('chapter/<int:index>/', ChapterDetailView.as_view(), name='chapter-detail'),
    path('chapter-comment/', ChapterCommentListView.as_view(), name='chapter-comment-list'),
    path('chapter-comment/<int:pk>/', ChapterCommentDeleteView.as_view(), name='chapter-comment-delete'),
    path('review-comment/', ReviewCommentListView.as_view(), name='review-comment-list'),
    path('review-comment/<int:pk>/', ReviewCommentDeleteView.as_view(), name='review-comment-delete'),
    path('review/', ReviewListView.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail')
]