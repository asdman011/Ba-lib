from django.contrib import admin
from .models import Book, ReadingProgress, Folder

# Register your models here
admin.site.register(Book)
admin.site.register(ReadingProgress)
admin.site.register(Folder)
