from django.contrib import admin

# Register your models here.
from .models import Cafe,Location,CafeLike,CafeKeyword
class LocationAdmin(admin.ModelAdmin):
    pass

class CafeAdmin(admin.ModelAdmin):
    pass

class CafeLikeAdmin(admin.ModelAdmin):
    pass

class CafeKeywordAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cafe,CafeAdmin)
admin.site.register(CafeLike,CafeAdmin)
admin.site.register(CafeKeyword,CafeAdmin)
admin.site.register(Location,LocationAdmin)
