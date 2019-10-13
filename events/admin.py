# -*- coding: utf-8 -*-

from django.contrib import admin
from django.db.models import Sum

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
    list_display = ("uuid", "event", "detail", "message", "guests", "confirmed")
    list_filter = ("event", "guests", "confirmed", "created_at", "updated_at")
    ordering = ("updated_at",)
    search_fields = ("uuid", "detail", "message", "event__title")
    readonly_fields = ("confirmed", "message")
