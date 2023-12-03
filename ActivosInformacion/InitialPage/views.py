from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from InitialPage.models import SubtypesActives, TypesActives

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        
        return render(request, "home/home.html")
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def typesActives(request):
    if request.user.is_authenticated:
        typesactives = TypesActives.objects.all()
        return render(request, "program/typesActives.html",{
            "typesactives": typesactives
        })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def subtypesActives(request):
    if request.user.is_authenticated:
        subtypesactives = SubtypesActives.objects.all()
        return render(request, "program/subtypesActives.html",{
            "subtypesactives": subtypesactives,
        })
    else:
        return HttpResponseRedirect(reverse("user:login"))