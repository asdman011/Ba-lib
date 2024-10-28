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
# backend/urls.py

import os
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from core import views as core_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', core_views.index, name='index'),  # Main index
    path('dashboard/', core_views.index, name='dashboard'),  # Renders React's index.html for dashboard
    path('books/', core_views.book_list, name='book_list'),  # Django views for books
    path('books/add/', core_views.add_book, name='add_book'),
    path('folders/', core_views.folder_list, name='folder_list'),  # Django views for folders
    path('profile/', core_views.profile, name='profile'),
        path('user/<int:user_id>/', core_views.user_profile, name='user_profile'),  # New route for viewing other profiles


    # Django views
    path('books/<int:book_id>/', core_views.book_detail, name='book_detail'),
    path('books/<int:book_id>/progress/', core_views.get_reading_progress, name='get_reading_progress'),
    path('books/<int:book_id>/progress/update/', core_views.update_reading_progress, name='update_reading_progress'),
    path('folders/<int:folder_id>/', core_views.folder_detail, name='folder_detail'),
    path('folders/create/', core_views.create_folder, name='create_folder'),
    path('folders/my/', core_views.my_folders, name='my_folders'),
    path('folders/public/', core_views.public_folders, name='public_folders'),
    path('profiles/public/', core_views.public_profiles, name='public_profiles'),
]

# Serve static files on dashboard route in development
if settings.DEBUG:
    urlpatterns += static("/dashboard/static/", document_root=os.path.join(settings.BASE_DIR, "frontend/build/static"))
    urlpatterns += static("/dashboard/manifest.json", document_root=os.path.join(settings.BASE_DIR, "frontend/build"))
    urlpatterns += static("/static/", document_root=os.path.join(settings.BASE_DIR, "frontend/build/static"))
    urlpatterns += static("/manifest.json", document_root=os.path.join(settings.BASE_DIR, "frontend/build"))