# -*- coding: utf-8 -*-
import django
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, re_path

urls_api = [path("api/v1/", include("events.urls"))]

urlpatterns = urls_api + [
    path("", admin.site.urls),
    re_path(
        "static/(.*)$",
        django.views.static.serve,
        {"document_root": settings.STATIC_ROOT},
    ),
    re_path(
        "media/(.*)$", django.views.static.serve, {"document_root": settings.MEDIA_ROOT}
    ),
]

if settings.DOCS:
    from rest_framework_swagger.views import get_swagger_view

    schema_view = get_swagger_view(title="Mishteh API", patterns=urls_api)
    urlpatterns += [path("docs/", schema_view)]
