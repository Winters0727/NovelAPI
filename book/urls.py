from django.urls import path

# from rest_framework import routers

from .views import BookListView, BookDetailView, ChapterListView, ChapterDetailView, \
ChapterCommentListView, ChapterCommentDeleteView

app_name = 'book'

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('chapter/', ChapterListView.as_view(), name='chapter-list'),
    path('chapter/<int:index>/', ChapterDetailView.as_view(), name='chapter-detail'),
    path('chapter/comment/', ChapterCommentListView.as_view(), name='chapter-comment-list'),
    path('chapter/comment/<int:pk>/', ChapterCommentDeleteView.as_view(), name='chapter-comment-delete'),
]