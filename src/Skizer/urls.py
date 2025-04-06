"""
URL configuration for Skizer project.
"""

from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", view=home_view, name="home"),
    path("about/", view=about_view, name="about"),
]
