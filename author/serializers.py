import os

from django.conf import settings
from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer

from .models import Author

class AuthorSerializer(UserDetailsSerializer):
    nickname = serializers.CharField(source="author.nickname")
    profile_image = serializers.ImageField(source="author.profile_image")
    
    class Meta(UserDetailsSerializer.Meta):
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