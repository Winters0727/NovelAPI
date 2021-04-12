from django.urls import path

# from rest_framework import routers

from .views import BookListView, BookDetailView, ChapterListView, ChapterDetailView, CommentListView, CommentDeleteView

urlpatterns = [
    path('book/', BookListView.as_view()),
    path('book/<int:pk>/', BookDetailView.as_view()),
    path('chapter/', ChapterListView.as_view()),
    path('chapter/<int:index>/', ChapterDetailView.as_view()),
    path('comment/', CommentListView.as_view()),
    path('comment/<int:pk>/', CommentDeleteView.as_view())
]