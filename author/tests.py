from django.test import TestCase
from django.contrib.auth.models import User

from .models import Author
# Create your tests here.

class CreateAuthorTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='winters', email='winters@gmail.com' , password='winters001!')

    def test_get_user_info(self):
        user = User.objects.get(id=1)
        user_username = user._meta.get_field('username').verbose_name
        user_email = user._meta.get_field('email').verbose_name
        print(user.author.profile_image)
        self.assertEquals(user_username, 'winters')
        self.assertEquals(user_email, 'winters@gmail.com')