from django.db import models
from User.models import Users
from Cafe.models import Cafe
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

class Review(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=80)
    content = models.CharField(max_length=1000)
    image = models.ImageField(blank=True, upload_to='review_images/%Y%m%d')
    star = models.IntegerField()
    mark = models.BooleanField(default=False)
    #created_at = models.DateTimeField(auto_now_add=True)
    
    
    keywords = models.TextField(null=True)
    

    cafe_id = models.ForeignKey(
        Cafe, on_delete=models.CASCADE, related_name="cafe_id")
    user_id = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name="Review_user")


class ReviewLike(models.Model):
    user_id = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name="ReviewLike_user")
    review_id = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="review_id")
