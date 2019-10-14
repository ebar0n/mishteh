# -*- coding: utf-8 -*-

from django.contrib import admin
from django.db.models import Sum
from django.utils.html import format_html
from django.urls import reverse

from events import models


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "datetime",
        "invitations",
        "confirmed",
        "guests",
        "created_at",
    )
    list_filter = ("datetime", "created_at")
    ordering = ("datetime",)
    search_fields = ("title",)

    def invitations(self, obj):
        return obj.invitations.count()

    def confirmed(self, obj):
        return obj.invitations.filter(confirmed=True).count()

    def guests(self, obj):
        return (
            obj.invitations.filter(confirmed=True)
            .aggregate(Sum("guests"))
            .get("guests__sum", 0)
        )


@admin.register(models.Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = (
        "uuid",
        "event",
        "detail",
        "message",
        "guests",
        "confirmed",
        "url",
        "account",
    )
    list_filter = ("event", "guests", "confirmed", "created_at", "updated_at")
    ordering = ("updated_at",)
    search_fields = ("uuid", "detail", "message", "event__title", "event__email")
    readonly_fields = ("confirmed", "message")

    def url(self, obj):
        url_api = reverse("Invitations-detail", args=[str(obj.uuid)])
        return format_html('<a href="{}" target="_blank">Link!</a>', url_api)
