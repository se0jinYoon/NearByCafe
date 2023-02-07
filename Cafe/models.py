from django.db import models
from User.models import User
from Review.models import Review
# Create your models here.


class Location(models.Model):
    location_name = models.CharField(max_length=32)
    latitude = models.FloatField(defalut=37.314964)
    longtitude = models.FloatField(defalut=126.575308)


class Cafe(models.Model):
    cafe_name = models.CharField(max_length=32)
    cafe_address = models.CharField(max_length=128)
    cafe_image = models.ImageField(upload_to="cafephoto/")
    cafe_runtime = models.CharField(max_length=48)
    cafe_menu = models.TextField()
    cafe_number = models.CharField(max_length=16)
    location_id = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    
    
class Keyword(models.Model):
    keyword_name = models.CharField(max_length=24)
    
    
class CafeKeyword(models.Model):
    keyword_id = models.ForeignKey(Keyword,related_name="keyword",on_delete=models.CASCADE)
    review_id = models.ForeignKey(Review,related_name="review",on_delete=models.CASCADE)
    cafe_id = models.ForeignKey(Cafe,related_name="cafe",on_delete=models.CASCADE)


class CafeLike(models.Model):
    user_id = models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)
    cafe_id = models.ForeignKey(Cafe,related_name="cafe",on_delete=models.CASCADE)
