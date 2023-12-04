from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from CompanyAssets.models import Origin

# Create your views here.
def companyassets(request):
    if request.user.is_authenticated:
        return render(request, "companyassets.html")
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def origin(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST["name"]
            description = request.POST["description"]
            origin = Origin(name=name, description=description)
            origin.save()
            origin = Origin.objects.all()
            return render(request, "origin.html",{
                "origin": origin
            })
        else:
            origin = Origin.objects.all()
            return render(request, "origin.html",{
                "origin": origin
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def editOrigin(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            id = request.POST["id"]
            name = request.POST["name"]
            description = request.POST["description"]
            origin = Origin.objects.get(id=id)
            origin.name = name
            origin.description = description
            origin.save()
            origin = Origin.objects.all()
            return render(request, "origin.html",{
                "origin": origin
            })
        else:
            origin = Origin.objects.all()
            return render(request, "origin.html",{
                "origin": origin
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def deleteOrigin(request, id):
    if request.user.is_authenticated:
        origin = Origin.objects.get(id=id)
        origin.delete()
        origin = Origin.objects.all()
        return render(request, "origin.html",{
            "origin": origin
        })
    else:
        return HttpResponseRedirect(reverse("user:login"))