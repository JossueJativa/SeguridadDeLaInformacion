from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def enterAsset(request):
    return render(request, "home/enterAsset.html")