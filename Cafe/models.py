from django.db import models
from User.models import User
from Review.models import Review
# Create your models here.

location=['a','b','c']
class Location(models.Model):
    Locations=[
        ('서울 전체','서울 전체'),
        ('왕십리/한양대/성수','왕십리/한양대/성수'),
        ('강남/역삼/선릉/압구정','강남/역삼/선릉/압구정'),
        ('건대입구/세종대','건대입구/세종대'),
        ('서울대입구/신림','서울대입구/신림'),
        ('동작/흑석/상도','동작/흑석/상도'),
        ('노량진/여의도/영등포/당산','노량진/여의도/영등포/당산'),
        ('구로/신도림','구로/신도림'),
        ('목동/양천/금천','목동/양천/금천'),
        ('광운대/공릉/노원/도봉','광운대/공릉/노원/도봉'),
        ('수유/미아','수유/미아'),
        ('김포공항/염창/강서','김포공항/염창/강서'),
        ('홍대/합정/망원/서강','홍대/합정/망원/서강'),
        ('신촌/이대/서대문/아현','신촌/이대/서대문/아현'),
        ('혜화/성균관대','혜화/성균관대'),
        ('청량리/회기','청량리/회기'),
        ('성신여대/안암/성북/길음','성신여대/안암/성북/길음'),
        ('잠실/송파/강동','잠실/송파/강동'),
        ('을지로/명동/중구','을지로/명동/중구'),
        ('서초/교대/사당','서초/교대/사당'),
        ('종로/인사동/동대문','종로/인사동/동대문'),
        ('서울역/이태원/용산','서울역/이태원/용산'),
        ('중랑/쌍봉','중랑/쌍봉'),
    ]
    name = models.CharField(max_length=32,choices=Locations)
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
    #keyword_name = models.CharField(max_length=24)



class CafeLike(models.Model):
    user_id = models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)
    cafe_id = models.ForeignKey(Cafe,related_name="cafe",on_delete=models.CASCADE)
