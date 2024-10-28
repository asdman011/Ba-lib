from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    pass

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField(default='2000-01-01')  # Define a default value
    current_page = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title

class Streak(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    streak_days = models.IntegerField(default=0)
class ReadingProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    current_page = models.IntegerField(default=0)
    last_read_date = models.DateTimeField(auto_now=True)
    streak_count = models.IntegerField(default=0)

    def update_streak(self):
        # Check if the last read date was yesterday to continue the streak
        today = timezone.now().date()
        if self.last_read_date.date() == today - timedelta(days=1):
            self.streak_count += 1
        elif self.last_read_date.date() < today - timedelta(days=1):
            # If it’s been more than a day since last read, reset streak
            self.streak_count = 1
        else:
            self.streak_count = max(1, self.streak_count)
        self.last_read_date = timezone.now()
        self.save()

    def __str__(self): #don't know if this is necessary
        return f"{self.user.username} - {self.book.title}"

class Folder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)  # Controls if folder is public or private

    def __str__(self):
        return f"{self.user.username} - {self.name}"
