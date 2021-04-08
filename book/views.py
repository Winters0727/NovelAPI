import os

from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework import generics, viewsets

from .models import Book, Chapter
from .serializers import BookSerializer, ChapterSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

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

class ChapterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    lookup_field = 'index'
    permission_classes = [IsAuthorOrReadOnly]