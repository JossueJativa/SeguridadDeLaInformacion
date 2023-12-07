from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def enterAsset(request):
    return render(request, "home/enterAsset.html")

def enterUsers(request):
    return render(request, "home/enterUsers.html")

def enterDepartment(request):
    return render(request, "home/enterDepartment.html")