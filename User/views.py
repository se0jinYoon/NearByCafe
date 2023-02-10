from django.shortcuts import redirect, render
from django.http.request import HttpRequest
from User.models import Users, School
from User.forms import SignupForm
from django.contrib import auth
from django.contrib import messages

# Create your views here.


def validate_username(username):  # 아이디 검증 메소드
    validate_condition = [
        lambda s: all(x.islower() or x.isdigit() for x in s),  # 영문자, 숫자 허용
        lambda s: any(x.islower() for x in s),  # 영어 소문자는 필수
        lambda s: len(s) == len(s.replace(" ", "")),
        lambda s: len(s) >= 6,
        lambda s: len(s) <= 20,
    ]

    for validator in validate_condition:
        if not validator(username):  # 하나라도 조건에서 False라면 True 반환
            return True


def validate_password(password):  # 비밀번호 검증 메소드
    validate_condition = [
        lambda s: all(x.islower() or x.isupper() or x.isdigit() or (x in [
                      '!', '@', '#', '$', '%', '^', '&', '*', '_']) for x in s),  # 영문자 대소문자, 숫자, 특수문자(리스트)만 허용
        lambda s: any(x.islower() or x.isupper() for x in s),  # 영어 대소문자 필수
        lambda s: len(s) == len(s.replace(" ", "")),
        lambda s: len(s) >= 8,  # 글자수 제한
        lambda s: len(s) <= 15,  # 글자수 제한
    ]

    for validator in validate_condition:
        if not validator(password):
            return True


def sign_up(request: HttpRequest, *args, **kwargs):

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, "mainpage.html")
        # else:
        if Users.objects.filter(username=request.POST['username']).exists():
            messages.error(request, '이미 사용 중인 아이디입니다.')
            return redirect('User:sign_up')
        if validate_username(request.POST['username']):
            messages.error(
                request, '올바른 아이디 형식을 입력해주세요. (영어 소문자 필수, 숫자, 8~20자)')
        if request.POST['password1'] != request.POST['password2']:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
            return redirect('User:sign_up')
        if validate_password(request.POST['password1']):
            messages.error(
                request, '올바른 비밀번호 형식을 입력해주세요. (영문 대소문자, 숫자, 특수문자 일부 허용)')

    # (기본, GET요청) 회원가입 페이지를 띄우기
    else:
        form = SignupForm()
        # 템플릿 이름은 임시로
        return render(request, 'signup_example.html', {"form": form})


# def activate(request, *args, **kwargs):
