from django.contrib import admin
from .models import Cafe, Location, CafeLike, CafeKeyword

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']

@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    list_display = ['name','image','address','image','keywords','runtime','menu','number','location_id','latitude','longtitude']

class CafeLikeAdmin(admin.ModelAdmin):
    pass

class CafeKeywordAdmin(admin.ModelAdmin):
    pass

admin.site.register(CafeLike)
admin.site.register(CafeAdmin)
admin.site.register(CafeKeyword)

