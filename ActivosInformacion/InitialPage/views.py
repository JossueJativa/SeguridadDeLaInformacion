from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, "home/home.html")
    else:
        return HttpResponseRedirect(reverse("user:login"))