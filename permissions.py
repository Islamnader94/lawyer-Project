from lawyer.models.user_model import Role, AccountUser
from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import ImproperlyConfigured
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.permissions import BasePermission

class CustomPermissions(BasePermission):
    """
    Allows access only to authenticated users.
    """
    permission_required = None
    def has_permission(self, request, view):
        # create a loop
        permission_required = view.permission_required
        return request.user.has_role_perms(permission_required)
      