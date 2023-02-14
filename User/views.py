from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

@login_required('/login')
def delete_user(request):
    context = {}
    if request.user.is_authenticated:
        if request.method == 'POST':
            request.user.delete()
            auth_logout(request)
        return redirect('Cafe:main')
    return render(request,'withdrawal.html',context)
  
        


# Create your views here.
