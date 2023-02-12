from django.shortcuts import render,redirect
from Review.models import *
from django.views.decorators.csrf import csrf_exempt
from Review.forms import ReviewForm
# Create your views here.
@csrf_exempt
def review_create(request):
    context = {}
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            ctx = {
                'form':form,
            }
            return render(request,"review_create.html",ctx)
    elif request.method == 'GET':
        form = ReviewForm()
        ctx = {
            'form' : form,
        }
        return render(request,"review_create.html",ctx)