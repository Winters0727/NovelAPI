from django.shortcuts import get_object_or_404

from rest_framework import serializers

from .models import Book, Chapter, ChapterComment, TemporaryChapter

from author.serializers import AuthorSerializer

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

class ChapterSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    book = BookSerializer(read_only=True)

    class Meta:
        model = Chapter
        fields = '__all__'

class ChapterCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChapterComment
        fields = '__all__'

class TemporaryChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemporaryChapter
        fields = '__all__'