import os
from PIL import Image
from io import BytesIO

from django.db.models import Q, F
from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Book, Chapter, ChapterComment
from .serializers import BookSerializer, ChapterSerializer, ChapterCommentSerializer
from .permissions import IsAuthor, IsBookAuthorOrReadOnly, IsChapterAuthorOrReadOnly, IsNotAnonymous

# Create your views here.
class BookListView(generics.ListCreateAPIView):
    # def post(self, request, *args, **kwargs):
    #     cover_image = Image.open(request.data.get('cover'))
    #     new_cover_image = cover_image.resize((100, 100))
    #     new_cover_image.save(os.path.join(settings.MEDIA_URL, 'cover-thumbnail', request.data.get("title"), f'{request.data.get("title")}-cover{os.path.splitext(request.data.get("cover").name)[1]}'))
    #     return self.create(request, *args, **kwargs)

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

class ChapterCommentListView(generics.ListCreateAPIView):
    def get_queryset(self):
        query = {
            "book__exact" : self.request.query_params.get('book'),
            "chapter__exact" : self.request.query_params.get('chapter'),
        }
        if len(query.values()) == list(query.values()).count(None):
            queryset = ChapterComment.objects.all().select_related('chapter')
        else:
            queryset = ChapterComment.objects.filter(**query)
        return queryset

    serializer_class = ChapterCommentSerializer
    permission_classes = [IsNotAnonymous]

class ChapterCommentDeleteView(generics.DestroyAPIView):
    queryset = ChapterComment.objects.all()
    serializer_class = ChapterCommentSerializer
    permission_classes = [IsAuthor]