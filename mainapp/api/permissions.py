from rest_framework.permissions import BasePermission


class AdminOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class OwnerOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user