from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Custom permission to only allow owners of an object to edit it.
    '''

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        # so we'll always allow GET, HEAD, or OPTIONS requests.

        if request.method in permissions.SAFE_METHODS:
            # permissions.SAFE_METHODS is a tuple containing HTTP methods
            # that are considered safe because they do not modify res
            # typically GET, HEAD, OPTIONS
            return True
        
        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
    
    
