from django.db import models
from User.models import Users
from Cafe.models import Cafe


class Review(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=80)
    content = models.CharField(max_length=1000)
    image = models.ImageField(blank=True, upload_to='review_images/%Y%m%d')
    star = models.IntegerField()
    mark = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    cafe_id = models.ForeignKey(
        Cafe, on_delete=models.CASCADE, related_name="cafe_id")
    user_id = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name="Review_user")


class ReviewLike(models.Model):
    user_id = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name="ReviewLike_user")
    review_id = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="review_id")
