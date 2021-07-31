from django.contrib.auth.models import User
from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user and obj.createdBy_id == request.user.id

class CanHandleReport(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('can_handle_report')

class CanCensorPost(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('censor_post')