from django.contrib import admin
from .models import Cafe,Location,CafeLike,CafeKeyword

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']

@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    list_display = ['name','image','address','image','runtime','menu','number','location_id']
# @admin.register(CafeKeyword)
# class CafeKeywordAdmin(admin.ModelAdmin):
#     list_display = ['name','review_id','cafe_id']
# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    pass

class CafeAdmin(admin.ModelAdmin):
    pass

class CafeLikeAdmin(admin.ModelAdmin):
    pass

class CafeKeywordAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Cafe,CafeAdmin)
# admin.site.register(CafeLike,CafeAdmin)
# admin.site.register(CafeKeyword,CafeAdmin)
# admin.site.register(Location,LocationAdmin)
