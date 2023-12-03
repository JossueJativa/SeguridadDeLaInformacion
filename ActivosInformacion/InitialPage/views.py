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
        # if request.method == "POST":
        typesactives = TypesActives.objects.all()
        return render(request, "program/typesActives.html",{
            "typesactives": typesactives
        })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def subtypesActives(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            namesubtype = request.POST.get("namesubtype")
            descriptionsubtype = request.POST.get("descriptionsubtype")
            typesactive = request.POST.get("typesactive")

            typesactive = TypesActives.objects.get(pk=typesactives)

            subtypeactive = SubtypesActives.objects.create(
                name=namesubtype,
                description=descriptionsubtype,
                typesactive=typesactive
            )
            subtypeactive.save()

            subtypesactives = SubtypesActives.objects.all()
            typesactives = TypesActives.objects.all()
            return render(request, "program/subtypesActives.html",{
                "subtypesactives": subtypesactives,
                "typesactives": typesactives
            })
        subtypesactives = SubtypesActives.objects.all()
        typesactives = TypesActives.objects.all()
        return render(request, "program/subtypesActives.html",{
            "subtypesactives": subtypesactives,
            "typesactives": typesactives
        })
    else:
        return HttpResponseRedirect(reverse("user:login"))