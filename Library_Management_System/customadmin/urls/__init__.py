# -*- coding: utf-8 -*-
from django.urls import include, path

from .. import views
from . import urls_auth, urls

urlpatterns = [
    path("", views.IndexView.as_view(), name="dashboard"),
    path("", include(urls_auth)),
    path("", include(urls)),
]