from django.shortcuts import render,redirect
from User.models import *
from django.contrib import auth
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
#이전 로직
# def login_page(request):
#     if request.method == "POST":
#             req_id = request['id']
#             req_passwd = request['passwd']
#             user = Users.objects.get(users_id = req_id)
#             if req_passwd == user.password: 
#                 request.session['login_session'] = user.users_id
#                 return redirect('')        
#         except KeyError:
#                 return HttpResponse(status=400)
@csrf_exempt
def login_page(request):
    
    if request.method == 'POST':
        users_id = request.POST['users_id']
        users_passwd = request.POST['password']
        # isidstorage = request.POST['isidstorage']
        # print(isidstorage)
        print(users_id)
        print(users_passwd)
        users = auth.authenticate(request,username=users_id, password=users_passwd)

            
        if users is not None:
            auth.login(request,users)
            request.session['login_session'] = users_id
            
            return redirect('/')   
        else:#로그인 실패 시 모달창 띄우는 분기
            print("failed")
            context = {'state' : 'false'}
            return render(request,'login.html',context)
    else:
        

        context = {
            
        }     
        return render(request, 'login.html',context)
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('/')

# Create your views here.
