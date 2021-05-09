from django.test import TestCase

from .models import Author
# Create your tests here.

class CreateAuthorTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(username='winters', email='winters@gmail.com' , password='winters001!')

    def test_get_user_info(self):
        author = Author.objects.get(id=1)
        self.assertEquals(author.username, 'winters')
        self.assertEquals(author.email, 'winters@gmail.com')