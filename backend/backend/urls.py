"""
URL configuration for backend project.

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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from core.views import index, profile
from core import views as core_views

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Include allauth URLs for OAuth
    path('', index, name='index'),
    path('login/', index, name='login'),
    path('dashboard/', index, name='dashboard'),
    path('signup/', index),
    path('books/<int:book_id>/progress/', core_views.get_reading_progress, name='get_reading_progress'),
    path('books/<int:book_id>/progress/update/', core_views.update_reading_progress, name='update_reading_progress'),
    path('folders/create/', core_views.create_folder, name='create_folder'),
    path('folders/my/', core_views.my_folders, name='my_folders'),
    path('folders/public/', core_views.public_folders, name='public_folders'),
    path('profiles/public/', core_views.public_profiles, name='public_profiles'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
