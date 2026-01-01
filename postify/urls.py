"""
URL configuration for postify project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # App routes
    path('tweet/', include('tweet.urls')),

    # Auth routes (login, logout, password reset)
    path('accounts/', include('django.contrib.auth.urls')),
]

# Media files (for development)
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
