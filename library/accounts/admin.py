from django.contrib import admin
from .models import CustomUser, BookBorrowed

admin.site.register(CustomUser)
admin.site.register(BookBorrowed)
