from django.shortcuts import render
from .models import Users
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


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