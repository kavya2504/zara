"""
URL configuration for zara project.

For more information, see:
https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin interface
    path('admin/', admin.site.urls),

    # Main app routes
    path('', include('mainapp.urls')),

    # Cart-related URLs
    path('cart/', include('cart.urls')),

    # Order and Payment URLs
    path('orders/', include('orders.urls')),
    path('payments/', include('payments.urls')),

    # Authentication routes
    path('accounts/', include('authentication.urls')),  # Custom login/signup
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in auth (login, logout, etc.)
]

# Serving media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)