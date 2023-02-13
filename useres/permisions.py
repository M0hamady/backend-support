from  rest_framework import permissions
from useres.models import User
from django.contrib.auth.backends import BaseBackend

class MyBackend(BaseBackend):
    def authenticate(self, request, token=None):
        # Check the token and return a user.
        if User.objects.get(user =request.user).is_manager:
            return True
        return False
        