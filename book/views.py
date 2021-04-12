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
from .permissions import IsAuthor, IsBookAuthorOrReadOnly, IsChapterAuthorOrReadOnly, IsNotAnonymous

# Create your views here.
class BookListView(generics.ListCreateAPIView):
    def get_queryset(self):
        query = {
            'author__exact' : self.request.query_params.get('author')
        }
        if len(query.values()) == list(query.values()).count(None):
            queryset = Book.objects.all()
        else:
            queryset = Book.objects.filter(**query)
        return queryset

    serializer_class = BookSerializer
    permission_classes = [IsNotAnonymous]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
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
    queryset = Chapter.objects.all()
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
            queryset = Comment.objects.all()
        else:
            queryset = Comment.objects.filter(**query)
        return queryset

    serializer_class = CommentSerializer
    permission_classes = [IsNotAnonymous]

class CommentDeleteView(generics.DestroyAPIView):
    def get_object(self, pk):
        comment_object = get_object_or_404(Comment, pk=pk)
        return comment_object
    serializer_class = CommentSerializer
    permission_classes = [IsAuthor]

# class ReviewListView(generics.ListCreateAPIView):
#     def get_queryset(self):
#         params = {
#             "author" : self.request.query_params.get('author'),
#             "book" : self.request.query_params.get('book'),
#         }
#         queryset = Review.objects.filter(Q(author__exact=params["author"]) & Q(book__exact=params["book"]))
#         return queryset
#     serializer_class = ReviewSerializer
#     permission_classes = [IsNotAnonymous]

# class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     permission_classes = [IsAuthorOrReadOnly]