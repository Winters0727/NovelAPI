import os

from django.db.models import Q, F
from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Book, Chapter, Comment, Review
from author.models import Author
from .serializers import BookSerializer, ChapterSerializer, CommentSerializer, ReviewSerializer
from .permissions import IsAuthor, IsBookAuthorOrReadOnly, IsChapterAuthorOrReadOnly, IsReviewAuthorOrReadOnly, IsNotAnonymous

# Create your views here.
class BookListView(generics.ListCreateAPIView):
    def get_queryset(self):
        query = {
            'author__exact' : self.request.query_params.get('author')
        }
        if len(query.values()) == list(query.values()).count(None):
            queryset = Book.objects.all().select_related('author')
        else:
            queryset = Book.objects.filter(**query)
        return queryset

    serializer_class = BookSerializer
    permission_classes = [IsNotAnonymous]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all().select_related('author')
    serializer_class = BookSerializer
    permission_classes = [IsBookAuthorOrReadOnly]

    def delete(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['pk'])
        cover_path = os.path.join(settings.MEDIA_ROOT, book.cover.name)
        os.remove(cover_path)
        return self.destroy(request, *args, **kwargs)

class ChapterListView(generics.ListCreateAPIView):
    def get_queryset(self):
        query = {
            'book__exact' : self.request.query_params.get('book')
        }
        if len(query.values()) == list(query.values()).count(None):
            queryset = Chapter.objects.all()
        else:
            queryset = Chapter.objects.filter(**query)
        return queryset

    serializer_class = ChapterSerializer
    permission_classes = [IsChapterAuthorOrReadOnly]

class ChapterDetailView(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, *args, **kwargs):
        chapter = get_object_or_404(Chapter, pk=kwargs['index'])
        chapter.view_count += 1
        chapter.save()
        return self.retrieve(request, *args, **kwargs)

    queryset = Chapter.objects.all().select_related('book')
    serializer_class = ChapterSerializer
    lookup_field = 'index'
    permission_classes = [IsChapterAuthorOrReadOnly]

class CommentListView(generics.ListCreateAPIView):
    def get_queryset(self):
        query = {
            "book__exact" : self.request.query_params.get('book'),
            "chapter__exact" : self.request.query_params.get('chapter'),
        }
        if len(query.values()) == list(query.values()).count(None):
            queryset = Comment.objects.all().select_related('chapter')
        else:
            queryset = Comment.objects.filter(**query)
        return queryset

    serializer_class = CommentSerializer
    permission_classes = [IsNotAnonymous]

class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthor]

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