from django.db import models
from User.models import User
from Review.models import Review
# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=32)
    latitude = models.FloatField(defalut=37.314964)
    longtitude = models.FloatField(defalut=126.575308)


class Cafe(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=128)
    image = models.ImageField(upload_to="cafephoto/")
    runtime = models.CharField(max_length=48)
    menu = models.TextField()
    number = models.CharField(max_length=16)
    location_id = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)


class CafeKeyword(models.Model):
    # Review : Cafe Keyword와 Keyword의 차이는 뭔가요?
    # Review : 현재 상태로는, 한 클래스로 합칠 수 있을 것 같습니다.
    CAFE_KEYWORDS=[
        ('데이트','데이트'),
        ('작업하기 좋은','작업하기 좋은'),
        ('공부하기 좋은','공부하기 좋은'),
        ('조용한','조용한'),
        ('시끌벅적한','시끌벅적한'),
        ('의자가 편한','의자가 편한'),
        ('디저트 맛있는','디저트 맛있는'),
        ('커피가 맛있는','커피가 맛있는'),
        ('저렴한','저렴한'),
        ('친절한','친절한'),
        ('혼카페','혼카페'),
        ('장소가 넓은','장소가 넓은'),
        ('콘센트가 많은','콘센트가 많은'),
        ('화장실 깨끗한','화장실 깨끗한'),
        ('인테리어 예쁜','인테리어 예쁜'),
        ]
    
    review_id = models.ForeignKey(Review,related_name="review",on_delete=models.CASCADE)
    cafe_id = models.ForeignKey(Cafe,related_name="cafe",on_delete=models.CASCADE)
    keyword_name = models.CharField(max_length=24)



class CafeLike(models.Model):
    user_id = models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)
    cafe_id = models.ForeignKey(Cafe,related_name="cafe",on_delete=models.CASCADE)
