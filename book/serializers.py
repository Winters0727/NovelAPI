from rest_framework import serializers

from .models import Book, Chapter, ChapterComment, TemporaryChapter

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class ChapterSerializer(serializers.ModelSerializer):
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