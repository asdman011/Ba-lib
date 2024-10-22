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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from core.views import index
from core import views as core_views

urlpatterns = [
    path('', index, name='index'),
    path('signup/', index),
    path('login/', index, name='login'),
    path('dashboard/', index, name='dashboard'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Include allauth URLs for OAuth
    path('profile/', core_views.profile, name='profile'),

    # Add more paths if necessary
]

urlpatterns = [
    path('admin/', admin.site.urls),
    # your other routes
] 

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
