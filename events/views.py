# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from django.urls import reverse

from events import mixins, models, serializers


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Events

    """

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ("datetime",)
    search_fields = ("title",)
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer


class InvitationViewSet(mixins.DefaultCRUDPermissions, viewsets.ModelViewSet):
    """
    ViewSet for Invitations

    """

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ("event", "guests", "confirmed")
    search_fields = ("event__title", "message")
    queryset = models.Invitation.objects.all()

    def get_serializer_class(self):
        if self.action in ["confirm", "not_confirm"]:
            return serializers.EmptySerializer

        return serializers.InvitationSerializer

    @action(detail=True, methods=["post"], name="Accept invitation")
    def confirm(self, request, *args, **kwargs):
        """
        Confirm Invitation

        """
        invitation = self.get_object()
        serializer = self.get_serializer_class()(data=request.data)

        if not serializer.is_valid():
            return Response({"errors": serializer.errors}, status.HTTP_400_BAD_REQUEST)

        invitation.confirmed = True
        invitation.message = serializer.data["message"]
        invitation.save(update_fields=["confirmed", "message", "updated_at"])

        return HttpResponseRedirect(
            reverse("Invitations-detail", args=[str(invitation.uuid)])
        )

    @action(
        detail=True,
        methods=["post"],
        name="Not Accept invitation",
        url_path="not-confirm",
    )
    def not_confirm(self, request, *args, **kwargs):
        """
        Not Confirm Invitation

        """
        invitation = self.get_object()
        serializer = self.get_serializer_class()(data=request.data)

        if not serializer.is_valid():
            return Response({"errors": serializer.errors}, status.HTTP_400_BAD_REQUEST)

        invitation.confirmed = False
        invitation.message = serializer.data["message"]
        invitation.save(update_fields=["confirmed", "message", "updated_at"])

        return HttpResponseRedirect(
            reverse("Invitations-detail", args=[str(invitation.uuid)])
        )
