from django.shortcuts import render

# Create your views here.
def profile(request, *args, **kwargs):

    context = {}
    return render(request, "profile.html", context=context)