from django.urls import path

# from rest_framework import routers

from .views import ReviewListView, ReviewDetailView, ReviewCommentListView, ReviewCommentDeleteView

app_name = 'review'

urlpatterns = [
    path('', ReviewListView.as_view(), name='review-list'),
    path('<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('comment/', ReviewCommentListView.as_view(), name='review-comment-list'),
    path('comment/<int:pk>/', ReviewCommentDeleteView.as_view(), name='review-comment-delete'),
]