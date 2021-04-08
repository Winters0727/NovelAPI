from django.http import Http404
from rest_framework import permissions

class IsIdentical(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user