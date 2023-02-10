from django.contrib import admin

# Register your models here.

from . import models


@admin.register(models.Users)
class CustomUserAdmin(admin.ModelAdmin):
    pass
