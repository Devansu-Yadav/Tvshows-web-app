from django.contrib import admin
from django.contrib.auth.models import User
from .models import Show, Profile
# Register your models here.

admin.site.register(Show)
admin.site.register(Profile)