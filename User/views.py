from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt

# @login_required('/')
@csrf_exempt
def delete_user(request):
    context = {}
    if request.user.is_authenticated:
        if request.method == 'POST':
            request.user.delete()
            auth_logout(request)
        # return redirect('Cafe:main')
        return render(request,'withdrawal.html',context)
  
    return render(request,'withdrawal.html',context)
  
        


# Create your views here.
