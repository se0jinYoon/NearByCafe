from django.contrib import admin
from Review.models import Review
# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['time','title','content','image','star','mark','cafe_id','user_id']
    list_display_links = ['time','title','content','image','star','mark','cafe_id','user_id']