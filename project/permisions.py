from  rest_framework import permissions

class IsAuthor(permissions.BasePermission):
    '''reqyest will check if user is the owner of project'''

    def has_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.au
    # pass