from django.db import models
from django.contrib.auth.models import AbstractUser


class School(models.Model):
    location_id = models.ForeignKey(
        'Cafe.Location', related_name="location_id", on_delete=models.SET_NULL, null=True)
    # REVIEW: school_이 붙을 이유는 없을 것 같습니다.
    name = models.CharField(max_length=16)
    email = models.CharField(max_length=16)  # 학교 이메일 도메인 변수명 변경


class Users(AbstractUser):
    school_id = models.ForeignKey(
        School, related_name="school_id", on_delete=models.SET_NULL, null=True)  # 학교 식별자[외래키]

    email_address = models.CharField(
        max_length=32, verbose_name="이메일")  # 이메일주소
    # users_id = models.CharField(max_length=20) # 아이디
    # password = models.CharField(max_length=16)  # 비밀번호
    realname = models.CharField(max_length=20, verbose_name="이름")
    nickname = models.CharField(max_length=32, verbose_name="닉네임")  # 랜덤 생성
    verified = models.BooleanField(default=False)  # 학교 인증여부 False or True, is_active로 변경 금지!

class Notice(models.Model):
    # REVIEW: Notice 모델에 notice_가 붙어있을 이유는 없을 것 같습니다.
    title = models.CharField(max_length=120)
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    user_name = models.CharField(max_length=16)
