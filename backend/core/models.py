# backend/core/models.py

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    pass

class Folder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_public = models.BooleanField(default=False)  # Controls if folder is public or private
    streak_count = models.IntegerField(default=0)   # Tracks streak specific to this folder
    last_read_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"

class Book(models.Model):
    folder = models.ForeignKey(Folder, related_name='books', on_delete=models.CASCADE, default=1)  # ID of a default Folder
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='book_covers/', blank=True, null=True)  # Cover image
    total_pages = models.IntegerField(default=1)  # Total number of pages with a default of 1
    current_page = models.IntegerField(default=0)
    comment = models.TextField(blank=True, null=True)  # Optional comment field
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def pages_left(self):
        return max(0, self.total_pages - self.current_page)

class ReadingProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, related_name='reading_progress', on_delete=models.CASCADE, default=1)  # ID of a default Folder
    general_streak = models.IntegerField(default=0)  # General streak across all folders
    last_read_date = models.DateField(null=True, blank=True)

    def update_general_streak(self):
        today = timezone.now().date()
        if self.last_read_date == today - timedelta(days=1):
            self.general_streak += 1
        elif self.last_read_date != today:
            self.general_streak = 1
        self.last_read_date = today
        self.save()
