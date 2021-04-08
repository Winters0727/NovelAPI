from django.urls import path

# from rest_framework import routers

from .views import BookListView, BookDetailView, ChapterListView, ChapterDetailView

urlpatterns = [
    path('book/', BookListView.as_view()),
    path('book/<int:pk>/', BookDetailView.as_view()),
    path('book/<int:pk>/chapter/', ChapterListView.as_view()),
    path('book/<int:pk>/chapter/<int:index>/', ChapterDetailView.as_view())
]