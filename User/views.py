from django.shortcuts import redirect, render
from django.http.request import HttpRequest
from User.models import Users, School
from User.forms import SignupForm
from django.contrib import auth
from django.contrib import messages
import re

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


def validate_email(email):
    pattern = re.compile(r'@([\w.]+)')
    match = pattern.search(email)
    if match:
        validate_condition = [
            'g.hongik.ac.kr',  # 홍익대
            'smu.kr',  # 상명대
            'ewhain.com',  # 이화여대
            'khu.ac.kr',  # 경희대
            'hufs.ac.kr',  # 한국외대
            'yonsei.ac.kr',  # 연세대
            'duksung.ac.kr',  # 덕성여대
            'sju.ac.kr',  # 세종대
            'uos.ac.kr',  # 서울시립대
            'dongduk.ac.kr',  # 동덕여대
            'kookmin.ac.kr',  # 국민대
            'snu.ac.kr',  # 서울대
            'sungshin.ac.kr',  # 성신여대
            'kw.ac.kr',  # 광운대
            'konkuk.ac.kr'  # 건국대
            'korea.ac.kr',  # 고려대
            'catholic.ac.kr',  # 가톨릭대
            'hanyang.ac.kr',  # 한양대
            'sogang.ac.kr',  # 서강대
            'cau.ac.kr',  # 중앙대
            'skku.edu',  # 성균관대
        ]
        if match.group(1) in validate_condition:
            return True
        else:
            return False
    else:
        return False


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
            return redirect('User:sign_up')

        if request.POST['password1'] != request.POST['password2']:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
            return redirect('User:sign_up')

        if validate_password(request.POST['password1']):
            messages.error(
                request, '올바른 비밀번호 형식을 입력해주세요. (영문 대소문자, 숫자, 특수문자 일부 허용)')
            return redirect('User:sign_up')

        if validate_email(request.POST['email_address']) == False:
            messages.error(request, '올바른 학교 이메일 형식을 입력해주세요.')
            return redirect('User:sign_up')
        else:
            messages.error(request, '비밀번호가 올바르지 않습니다.')
            messages.error(
                request, '생성하신 비밀번호가 8자리 이상이며, 문자로만 이루어지지 않았는지 확인해주세요.')
            return redirect('User:sign_up')

    # (기본, GET요청) 회원가입 페이지를 띄우기
    else:
        form = SignupForm()
        # 템플릿 이름은 임시로
        return render(request, 'signup_example.html', {"form": form})


# def activate(request, *args, **kwargs):
