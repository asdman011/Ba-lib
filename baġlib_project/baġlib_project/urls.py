"""
URL configuration for baġlib_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin
from django.contrib.auth import views as auth_views
from core import views as core_views  # Import views from core

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', core_views.index, name='signup'),
    path('profile/', core_views.index, name='profile'),  # Route for profile
    path('dashboard/', core_views.index, name='dashboard'),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),  # Catch-all route
]

# Serve media files during development
if settings.DEBUG:  # Only serve static files in debug mode
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)