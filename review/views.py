from django.db.models import Q, F
from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Review, ReviewComment, TemporaryReview
from .serializers import ReviewSerializer, ReviewCommentSerializer, TemporaryReviewSerializer
from .permissions import IsAuthor, IsReviewAuthorOrReadOnly, IsNotAnonymous

# Create your views here.

class ReviewListView(generics.ListCreateAPIView):
    def get_queryset(self):
        query = {
            "author__exact" : self.request.query_params.get('author'),
            "book__exact" : self.request.query_params.get('book'),
        }
        if len(query.values()) == list(query.values()).count(None):
            queryset = Review.objects.filter(**query)
        else:
            queryset = Review.objects.all().select_related('book')
        return queryset
    serializer_class = ReviewSerializer
    permission_classes = [IsNotAnonymous]

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, *args, **kwargs):
        review = get_object_or_404(Review, pk=kwargs['pk'])
        review.view_count += 1
        review.save()
        return self.retrieve(request, *args, **kwargs)

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]

class ReviewCommentListView(generics.ListCreateAPIView):
    def get_queryset(self):
        query = {
            "review__exact" : self.request.query_params.get('review'),
        }
        if len(query.values()) == list(query.values()).count(None):
            queryset = ReviewComment.objects.all().select_related('review')
        else:
            queryset = ReviewComment.objects.filter(**query)
        return queryset

    serializer_class = ReviewCommentSerializer
    permission_classes = [IsNotAnonymous]

class ReviewCommentDeleteView(generics.DestroyAPIView):
    queryset = ReviewComment.objects.all()
    serializer_class = ReviewCommentSerializer
    permission_classes = [IsAuthor]

class TemporaryReviewListView(generics.ListCreateAPIView):
    def get_queryset(self):
        query = {
            "author__exact" : self.request.query_params.get('author'),
            "book__exact" : self.request.query_params.get('book'),
        }
        if len(query.values()) == list(query.values()).count(None):
            queryset = TemporaryReview.objects.filter(**query)
        else:
            queryset = TemporaryReview.objects.all().select_related('book')
        return queryset
    serializer_class = TemporaryReviewSerializer
    permission_classes = [IsAuthor]

class TemporaryReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, *args, **kwargs):
        review = get_object_or_404(TemporaryReview, pk=kwargs['pk'])
        review.view_count += 1
        review.save()
        return self.retrieve(request, *args, **kwargs)

    queryset = TemporaryReview.objects.all()
    serializer_class = TemporaryReviewSerializer
    permission_classes = [IsAuthor]
