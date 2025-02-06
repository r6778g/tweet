"""
URL configuration for the Mohit project.

The `urlpatterns` list routes URLs to views. For more details, visit:
https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin panel
    path("secure-admin/", admin.site.urls),

    # Tweet application URLs
    path("tweet/", include('tweet.urls')),

    # Authentication URLs (login, logout, password reset)
    path("accounts/", include('django.contrib.auth.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
