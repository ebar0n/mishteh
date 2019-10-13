# -*- coding: utf-8 -*-
from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from events import views

router = routers.DefaultRouter()

router.register(r"events", views.EventViewSet, "events")
router.register(r"invitations", views.InvitationViewSet, "Invitations")

urlpatterns = [path("", include(router.urls))]
