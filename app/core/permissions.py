from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    """
    Allows access only for admins or for own data.
    """

    def has_permission(self, request, view):
        return bool((str(request.user.id) == request.query_params.get("user_id")) or
                    request.user and request.user.is_staff and request.user.is_superuser)
