from django.shortcuts import render

# Create your views here.
def review_create(request, *args, **kwargs):

    context = {}
    return render(request, "review_create.html", context=context)