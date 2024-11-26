from django.contrib import admin

# Register your models here.

from .models import Author, Photo

admin.site.register([Author, Photo])