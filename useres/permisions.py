from rest_framework.permissions import BasePermission

from useres.models import User

class IsManager(BasePermission):
    """
    Allows access only to manager users.
    """

    def has_permission(self, request, view):
        return bool(request.user and User.objects.get(user = request.user).is_manager)
class IsEng(BasePermission):
    """
    Allows access only to engineer users.
    """

    def has_permission(self, request, view):
        return bool(request.user and User.objects.get(user = request.user).is_eng)
