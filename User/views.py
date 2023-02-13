
# 메일 인증 관련 import
from User.email_helper import send_mail
from django.forms import ValidationError
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.shortcuts import redirect, render
from django.http.request import HttpRequest
from User.models import Users, School
from User.forms import SignupForm
from django.contrib import auth
from django.contrib import messages
from django.shortcuts import render
from .models import Users
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import re
import random

@csrf_exempt
def find_pw2(request):
    req=json.loads(request.body)
    find_email=req['find_email']#사용자가 찾기위해 입력한 이메일
    
    try:
        selected_email=Users.objects.get(email_address=find_email)
        
    except:#find_email과 동일한 메일 db에 없을때
        findOrNot=False
    else:
        findOrNot=True
        
    finally:
        context={{"findOrNot":findOrNot, "find_email":find_email}}
        return JsonResponse(context)
    
@csrf_exempt    
def find_pw(request):
    find_email=request.GET.get('find_email')
    try:
        selected_email=Users.objects.get(email_address=find_email)
        
    except:
        selected_email=None
        
    if find_email is None:
        overlap="fail"
    else:overlap="pass"
    context={'overlap':overlap}
    return JsonResponse(context)

def findpw_page(request, *args, **kwargs):

    context = {}
    return render(request, "findpw.html", context=context)








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

            'naver.com',  # 테스트용 네이버
        ]
        if match.group(1) in validate_condition:
            return True
        else:
            return False
    else:
        return False


def make_random_nickname():
    seed1 = ['차가운', '따뜻한', '산뜻한', '다정한', '아늑한',
             '열정적인', '멋있는', '아름다운', '사랑스러운', '자신있는']
    seed2 = ['호랑이', '토끼', '원숭이', '염소', '코끼리', '오리', '사자', '슈빌', '공작', '타조']
    seed3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    rand1 = random.choice(seed1)
    rand2 = random.choice(seed2)
    rand3 = random.choice(seed3)
    return rand1+rand2+rand3


def sign_up(request: HttpRequest, *args, **kwargs):

    if request.method == "POST":
        form = SignupForm(request.POST)
        if validate_email(request.POST['email_address']) == False:
            messages.error(request, '올바른 학교 이메일 형식을 입력해주세요.')
            return redirect('User:sign_up')

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

        if form.is_valid():
            user = form.save()
            verify_email(request, form)
            return redirect('User:mail_notice')  # 인증메일 발송 안내 페이지로 리다이렉트

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
        return redirect('Cafe:main')

    messages.error(request, '메일 인증에 실패하였습니다.')
    return redirect('Cafe:main')


def mail_notice(request):

    return render(request, 'send_mail.html')

