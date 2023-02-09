from django.db import models
from User.models import User
from Cafe.models import Cafe, Keyword

class Review(models.Model):
    time=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=80)
    content=models.CharField(max_length=1000)
    image=models.ImageField(blank=True,upload_to='review_images/%Y%m%d')
    star=models.IntegerField()
    mark=models.BooleanField()
    
    cafe_id=models.ForeignKey(Cafe,on_delete=models.CASCADE,related_name="cafe_id")
    #keyword_id=models.ForeignKey(Keyword,on_delete=models.CASCADE,related_name="keyword_id")
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_id")
    
    
class ReviewLike(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_id")
    review_id=models.ForeignKey(Review,on_delete=models.CASCADE,related_name="review_id")
    
    
    
    
