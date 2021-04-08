import os

from django.conf import settings
from django.http import Http404
from rest_framework import mixins
from rest_auth.views import UserDetailsView

from .permissions import IsIdentical
# Create your views here.

class AuthorDetailView(UserDetailsView, mixins.DestroyModelMixin):
    permission_classes = [IsIdentical]

    def delete(self, request, *args, **kwargs):
        author = self.request.user.author
        profile_image_path = os.path.join(settings.MEDIA_ROOT, author.profile_image.name)
        os.remove(profile_image_path)
        return self.destroy(request, *args, **kwargs)