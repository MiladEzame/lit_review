from django.contrib import admin

# Register your models here.
from .models import UserFollows

admin.site.register(UserFollows)