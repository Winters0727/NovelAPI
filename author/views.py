import os

from django.conf import settings
from django.http import Http404
from rest_framework import mixins, status
from rest_framework.response import Response
from rest_auth.views import UserDetailsView
from rest_auth.registration.views import RegisterView

from .models import Author
from .serializers import AuthorSerializer, AuthorRegisterSerializer
from .permissions import IsIdentical
# Create your views here.

class AuthorRegisterView(RegisterView):
    queryset = Author.objects.all()
    serializer_class = AuthorRegisterSerializer

class AuthorDetailView(UserDetailsView, mixins.DestroyModelMixin):
    serializer_class = AuthorSerializer
    permission_classes = [IsIdentical]

    def delete(self, request, *args, **kwargs):
        author = self.request.user
        profile_image_path = os.path.join(settings.MEDIA_ROOT, author.profile_image.name)
        os.remove(profile_image_path)
        return self.destroy(request, *args, **kwargs)