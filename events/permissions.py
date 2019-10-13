# -*- coding: utf-8 -*-
from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """
    Returns true if the request.user is Admin

    """

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.

        :return: bool
        """
        if request.user.is_authenticated:
            if request.user.is_staff:
                return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.

        :return: bool
        """
        if request.user.is_authenticated:
            if request.user.is_staff:
                return True
        return False
