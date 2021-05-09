from django.test import TestCase

from author.models import Author
from .models import Book, Chapter

# Create your tests here.

class CreateBook(TestCase):
    @classmethod
    def setUpTestData(cls):
        author_one = Author.objects.create(
            username="winters",
            email="winters@gmail.com",
            password="winters001!"
        )

        book_one = Book.objects.create(
            author=author_one,
            title="이세계 코더"
        )

        book_one_chapter = Chapter.objects.create(
            index=1,
            title="코더, 이세계에 가다.",
            author=author_one,
            book=book_one,
            content="코더가 이세계에 가다. 그래서 코딩을 하냐고?"
        )

        author_two = Author.objects.create(
            username="jack",
            email="jack@gmail.com",
            password="jack001!"
        )

        book_two = Book.objects.create(
            author=author_two,
            title="이세계 프로그래머"
        )

        book_two_chapter = Chapter.objects.create(
            index=1,
            title="프로그래머, 이세계에 가다.",
            author=author_two,
            book=book_two,
            content="프로그래머가 이세계에 가다. 그래서 프로그래밍을 하냐고?"
        )

    def test_get_book_info(self):
        book = Book.objects.get(id=1)
        chapter = Chapter.objects.get(id=1)
        self.assertEqual(book, chapter.book)
        self.assertEqual(book.author, chapter.author)