from django.contrib import admin
from .models import Location

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name','latitude','longtitude']
    list_display_links = ['name','latitude','longtitude']


# Register your models here.
