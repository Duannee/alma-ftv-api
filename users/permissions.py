from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


class isSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated and request.user.is_superuser
        )


class isStudent(BasePermission):
    def has_permission(self, request, view):
        if (
            hasattr(request.user, "students")
            and request.user.students.exists()
            or request.user.is_superuser
        ):
            return True
        raise PermissionDenied("You must be a student to access this resource")
