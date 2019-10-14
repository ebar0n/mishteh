# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _
from rest_framework import serializers

from events import models


class EventSerializer(serializers.ModelSerializer):
    """
    Event Serializer

    """

    class Meta:
        """
        Meta

        """

        model = models.Event
        fields = (
            "title",
            "image",
            "description",
            "datetime",
            "place_address",
            "place_map",
        )


class InvitationSerializer(serializers.ModelSerializer):
    """
    Invitation Serializer

    """

    event = EventSerializer(many=False)

    class Meta:
        """
        Meta

        """

        model = models.Invitation
        fields = ("uuid", "event", "detail", "guests", "confirmed")


class EmptySerializer(serializers.Serializer):
    """
    Empty Serializer

    """

    message = serializers.CharField()
