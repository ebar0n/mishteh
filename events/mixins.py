# -*- coding: utf-8 -*-
from rest_framework import permissions

from events.permissions import IsAdmin


class DefaultCRUDPermissions(object):
    """
    Mixin to verify if the user can access to a method through a web service

    """

    def get_permissions(self):
        """
        Get permissions

        """
        if self.action in ["create", "update", "partial_update", "list", "destroy"]:
            return [IsAdmin()]

        if self.action in ["retrieve", "confirm", "not_confirm"]:
            return [permissions.AllowAny()]

        return [permission() for permission in self.permission_classes]
