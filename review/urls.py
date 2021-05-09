from django.urls import path

# from rest_framework import routers

from .views import ReviewListView, ReviewDetailView, ReviewCommentListView, ReviewCommentDeleteView, \
    TemporaryReviewListView, TemporaryReviewDetailView

app_name = 'review'

urlpatterns = [
    path('', ReviewListView.as_view(), name='review-list'),
    path('<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('comment/', ReviewCommentListView.as_view(), name='review-comment-list'),
    path('comment/<int:pk>/', ReviewCommentDeleteView.as_view(), name='review-comment-delete'),
    path('temporary/', TemporaryReviewListView.as_view(), name='review-temp-list'),
    path('temporary/<int:pk>/', TemporaryReviewDetailView.as_view(), name='review-temp-detail'),
]