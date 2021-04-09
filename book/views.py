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
from .permissions import IsAuthor, IsAuthorOrReadOnly, IsNotAnonymous

# Create your views here.
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsNotAnonymous]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def delete(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['pk'])
        cover_path = os.path.join(settings.MEDIA_ROOT, book.cover.name)
        os.remove(cover_path)
        return self.destroy(request, *args, **kwargs)

class ChapterListView(generics.ListCreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [IsNotAnonymous]

class ChapterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    lookup_field = 'index'
    permission_classes = [IsAuthorOrReadOnly]

class CommentListView(generics.ListCreateAPIView):
    def get_queryset(self):
        params = {
            "book" : self.request.query_params.get('book'),
            "chapter" : self.request.query_params.get('chapter'),
        }
        queryset = Comment.objects.filter(Q(book__exact=params["book"]) & Q(chapter__exact=params["chapter"]))
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