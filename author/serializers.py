import os

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from rest_framework import status, serializers
from rest_framework.response import Response

from rest_auth.serializers import UserDetailsSerializer
from rest_auth.registration.serializers import RegisterSerializer

from allauth.socialaccount.models import SocialAccount
from allauth.account import app_settings as allauth_settings
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.utils import get_username_max_length

from .models import Author

class AuthorRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=20)
    profile_image = serializers.ImageField(required=False, allow_empty_file=True)

    class Meta:
        model = Author
        fields = ('username', 'nickname', 'email', 'profile_image', )

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def custom_signup(self, request, user):
        pass

    def save(self, request):
        adapter = get_adapter()
        self.cleaned_data = self.get_cleaned_data()
        self.cleaned_data['nickname'] = request.data['nickname']
        self.cleaned_data['profile_image'] = request.data['profile_image'] if 'profile_image' in request.data.keys() else os.path.join('profile', 'default.png')
        author = Author.objects.create_user(**self.cleaned_data)
        adapter.save_user(request, author, self)
        self.custom_signup(request, author)
        setup_user_email(request, author, [])
        return author

class AuthorSerializer(UserDetailsSerializer):
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_settings.USERNAME_MIN_LENGTH,
        required=allauth_settings.USERNAME_REQUIRED
    )
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    nickname = serializers.CharField()
    profile_image = serializers.ImageField()
    
    class Meta(UserDetailsSerializer.Meta):
        model = Author
        fields = ('username', 'nickname', 'email', 'profile_image', )
        read_only_fields = ('username', 'email', )

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('author', {})
        nickname = profile_data.get('nickname')
        profile_image = profile_data.get('profile_image')

        instance = super(AuthorSerializer, self).update(instance, validated_data)

        profile = instance.author
        
        profile_image_path = os.path.join(settings.MEDIA_ROOT, profile.profile_image.name)
        os.remove(profile_image_path)

        if profile_data and nickname and profile_image:
            profile.nickname = nickname
            profile.profile_image = profile_image
            profile.save()
        return instance