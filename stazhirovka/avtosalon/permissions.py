from rest_framework import permissions


class IsAdminReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user

class ManagerOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and hasattr(request.user, "manager"):
            return True
        return False


class BuyerOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and hasattr(request.user, "buyer"):
            return True
        return False
