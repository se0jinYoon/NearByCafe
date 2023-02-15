from django.contrib import admin
from .models import Location,Cafe,CafeKeyword

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']

@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    list_display = ['name','image','address','image','runtime','menu','number','location_id','latitude','longtitude']
# @admin.register(CafeKeyword)
# class CafeKeywordAdmin(admin.ModelAdmin):
#     list_display = ['name','review_id','cafe_id']
# Register your models here.
