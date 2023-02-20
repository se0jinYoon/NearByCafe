from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.shortcuts import redirect, render, reverse
from django.http.request import HttpRequest

from User.models import Users, School
from User.models import *
from User.forms import SignupForm
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from User.email_helper import send_mail
from django.forms import ValidationError
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

import json
import re
import random


# 로그인 페이지
@csrf_exempt
def login_page(request):
    if request.method == 'POST':
        users_id = request.POST.get('users_id')
        users_passwd = request.POST.get('password')

        if request.POST.get('isidstorage'):
            request.session['login_session'] = users_id
            request.session['isidstorage'] = True
        else:
            request.session.pop('login_session', None)
            request.session.pop('isidstorage', None)

        print(users_id)
        print(users_passwd)

        users = auth.authenticate(
            request, username=users_id, password=users_passwd)
        context = {
            "recent_login_id": request.session.get('login_session'),
            "isidstorage": request.session.get('isidstorage')
        }

        if users is not None:
            # 만약 이메일 인증을 하지 않았을 때 분기 : verified field로 확인
            current_user = Users.objects.get(username=users_id).verified
            if current_user:  # True
                print("user")
                auth.login(request, users)
                # messages.info(request, "로그인이 완료되었습니다.")
                return redirect('/')

            else:  # False, 이메일 전송 페이지로 유저 정보와 함께 넘김
                user_email = Users.objects.get(username=users_id).email_address
                user_name = Users.objects.get(username=users_id).username
                verify_email_later(
                    request, user_name=user_name, user_email=user_email)

                # admin 테스트 할꺼면 이렇게 렌더로 받아봐야함
                # return render(request, 'send_mail.html', {'current_user': Users.objects.get(username=users_id)})

                url = reverse('User:mail_notice', kwargs={
                              'user_name': user_name, 'user_email': user_email})
                return redirect(url)  # 인증메일 발송 안내 페이지로 리다이렉트

        elif users is None:  # 로그인 실패 시 모달창 띄우는 분기
            print("failed")
            messages.error(
                request, '아이디 또는 비밀번호를 잘못 입력 했습니다.'
            )
            print(context['isidstorage'])
            return render(request, 'login.html', context=context)
    else:
        # 아이디 저장 체크되어 있으면 세션으로 저장

        context = {
            "recent_login_id": request.session.get('login_session'),
            "isidstorage": request.session.get('isidstorage')
        }
        print(context['isidstorage'])

        return render(request, 'login.html', context=context)


# 로그아웃 페이지
def logout_page(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            auth_logout(request)
        return redirect('/')


# 프로필 페이지
def profile(request, *args, **kwargs):

    if request.user.is_authenticated:
        user = Users.objects.get(username=request.user)
        email_address = user.email_address
        nickname = user.nickname
        context = {'email_address': email_address, 'nickname': nickname}

    else:
        return redirect('Cafe:main')

    return render(request, "profile.html", context=context)


# 비밀번호 찾기 메소드-form 이용
def findpw(request: HttpRequest, *args, **kwargs):
    context = {}
    if request.method == "POST":
        if Users.objects.filter(email_address=request.POST['find_pw_email']).exists():
            user = Users.objects.get(
                email_address=request.POST['find_pw_email'])
            print(user)
            name = user.username
            email = user.email_address

            messages.error(request, '해당 이메일로 비밀번호 재설정 링크를 보냈습니다. ')
            verify_email_later(request, name, email)

            return redirect('User:findpw')
        else:
            messages.error(request, '가입 이력이 존재하지 않는 이메일 입니다.')
            return redirect('User:findpw')

    return render(request, 'findpw.html', context=context)


# 아이디 검증 메소드
def validate_username(username):
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


# 비밀번호 검증 메소드
def validate_password(password):
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


# 이메일 검증 메소드
def validate_email(email):
    pattern = re.compile(r'@([\w.]+)')
    match = pattern.search(email)

    if match:
        validate_condition = [
            'g.hongik.ac.kr',  # 홍익대
            'smu.kr',  # 상명대
            'ewhain.net',  # 이화여대
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

            'naver.com',  # 테스트용 네이버
        ]
        if match.group(1) in validate_condition:
            return True
        else:
            return False
    else:
        return False


# 닉네임 랜덤 생성 메소드
def make_random_nickname():
    seed1 = ['차가운', '따뜻한', '산뜻한', '다정한', '아늑한',
             '열정적인', '멋있는', '아름다운', '사랑스러운', '자신있는']
    seed2 = ['호랑이', '토끼', '원숭이', '염소', '코끼리', '오리', '사자', '슈빌', '공작', '타조']
    seed3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    rand1 = random.choice(seed1)
    rand2 = random.choice(seed2)
    rand3 = random.choice(seed3)
    return rand1+rand2+rand3


# 회원 가입
def sign_up(request: HttpRequest, *args, **kwargs):

    if request.method == "POST":
        form = SignupForm(request.POST)

        if validate_email(request.POST['email_address']) == False:
            messages.error(request, '올바른 학교 이메일 형식을 입력해주세요.')
            return redirect('User:sign_up')

        if Users.objects.filter(username=request.POST['username']).exists():
            messages.error(request, '이미 사용 중인 아이디입니다.')
            return redirect('User:sign_up')

        if Users.objects.filter(username=request.POST['email_address']).exists():
            messages.error(request, '이미 사용 중인 이메일입니다.')
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

        # if len(request.POST.getlist('agree1')) == 0:
        #     messages.error(
        #         request, '이용 약관에 동의해주세요.')
        #     return redirect('User:sign_up')

        # if len(request.POST.getlist('agree2')) == 0:
        #     messages.error(
        #         request, '개인정보 수집 및 이용에 동의해주세요.')
        #     return redirect('User:sign_up')

        # if len(request.POST.getlist('agree3')) == 0:
        #     messages.error(
        #         request, '위치 기반 서비스 이용약관에 동의해주세요.')
        #     return redirect('User:sign_up')

        if form.is_valid():
            user = form.save()
            verify_email(request, form)

            url = reverse('User:mail_notice', kwargs={
                          'user_name': request.POST['username'],
                          'user_email': request.POST['email_address']})
            return redirect(url)  # 인증메일 발송 안내 페이지로 리다이렉트

        else:
            messages.error(request, '비밀번호가 올바르지 않습니다.')
            messages.error(
                request, '생성하신 비밀번호가 8자리 이상이며, 문자로만 이루어지지 않았는지 확인해주세요.')
            return redirect('User:sign_up')

    # (기본, GET요청) 회원가입 페이지를 띄우기
    else:
        form = SignupForm()
        # 템플릿 이름은 임시로
        return render(request, 'signup_cj.html', {"form": form})


# 인증 메일 전송
def verify_email(request, form, *args, **kwargs):
    object = form.save()
    print(object)
    print(' ------------------ SEND THE EMAIL!..')

    print(f'object.username is {object.username}')
    print(f'object.email is {object.email_address}')
    print(f'object.nickname is {object.nickname}')
    send_mail(
        '{}님의 회원가입 인증메일 입니다.'.format(object.username),
        [object.email_address],
        html=render_to_string('register_email.html', {
            'user': object,
            'uid': urlsafe_base64_encode(force_bytes(object.pk)).encode().decode(),
            'domain': request.META['HTTP_HOST'],
            'token': default_token_generator.make_token(object),
        }),
    )

# 인증 메일 전송(추후 로그인 과정 시)


def verify_email_later(request, user_name, user_email, *args, **kwargs):
    object = Users.objects.get(username=user_name)
    print(object)
    print(' ------------------ SEND THE EMAIL!..')

    print(f'object.username is {object.username}')
    print(f'object.email is {object.email_address}')

    send_mail(
        '{}님의 회원가입 인증메일 입니다.'.format(user_name),
        [user_email],
        html=render_to_string('register_email.html', {
            'user': object,
            'uid': urlsafe_base64_encode(force_bytes(object.pk)).encode().decode(),
            'domain': request.META['HTTP_HOST'],
            'token': default_token_generator.make_token(object),
        }),
    )


# 계정 활성화
def activate(request, uid64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        current_user = Users.objects.get(pk=uid)
        print(f'current_user is ... {current_user}')
    except (TypeError, ValueError, OverflowError, Users.DoesNotExist, ValidationError):
        messages.error(request, '메일 인증에 실패했습니다.')
        return redirect('Cafe:main')

    if default_token_generator.check_token(current_user, token):
        current_user.verified = True
        current_user.nickname = make_random_nickname()
        current_user.save()

        messages.info(request, '메일 인증이 완료되었습니다.')
        return redirect('User:login')

    messages.error(request, '메일 인증에 실패하였습니다.')
    return redirect('User:login')


# 안내 메일 페이지
def mail_notice(request, user_name=None, user_email=None):
    print(user_name)
    print(user_email)

    if request.method == "POST":
        verify_email_later(request, user_name=user_name, user_email=user_email)
    return render(request, 'send_mail.html')


@csrf_exempt
def delete_user(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            request.user.delete()
            auth_logout(request)
            return redirect('Cafe:main')
        else:
            return render(request, 'withdrawal.html')
    else:
        return redirect("Cafe:main")
