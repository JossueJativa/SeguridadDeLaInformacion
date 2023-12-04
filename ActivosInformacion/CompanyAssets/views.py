from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from CompanyAssets.models import Origin, CompanyAssets

# Create your views here.
def companyassets(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get("name")
            description = request.POST.get("description")
            ubication = request.POST.get("ubication")
            quantity = request.POST.get("quantity")
            notes = request.POST.get("notes")
            typeofasset = request.POST.get("typeofasset")
            origin = request.POST.get("typesorigin")

            origin = Origin.objects.get(pk=origin)
            companyassets = CompanyAssets(
                name=name, 
                description=description, 
                ubication=ubication, 
                quantity=quantity, 
                notes=notes, 
                typeofasset=typeofasset, 
                origin=origin
            )
            companyassets.save()
            companyassets = CompanyAssets.objects.all()
            origin = Origin.objects.all()
            return render(request, "companyassets.html",{
                "companyassets": companyassets,
                "origin": origin
            })
        else:
            companyassets = CompanyAssets.objects.all()
            origin = Origin.objects.all()
            return render(request, "companyassets.html",{
                "companyassets": companyassets,
                "origin": origin
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def editCompanyAssets(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            id = request.POST.get("id")
            name = request.POST.get("name")
            description = request.POST.get("description")
            ubication = request.POST.get("ubication")
            quantity = request.POST.get("quantity")
            notes = request.POST.get("notes")
            typeofasset = request.POST.get("typeofasset")
            origin = request.POST.get("typesorigin")

            origin = Origin.objects.get(pk=origin)
            companyassets = CompanyAssets.objects.get(pk=id)
            companyassets.name = name
            companyassets.description = description
            companyassets.ubication = ubication
            companyassets.quantity = quantity
            companyassets.notes = notes
            companyassets.typeofasset = typeofasset
            companyassets.origin = origin
            companyassets.save()
            companyassets = CompanyAssets.objects.all()
            origin = Origin.objects.all()
            return render(request, "companyassets.html",{
                "companyassets": companyassets,
                "origin": origin
            })
        else:
            companyassets = CompanyAssets.objects.all()
            origin = Origin.objects.all()
            return render(request, "companyassets.html",{
                "companyassets": companyassets,
                "origin": origin
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def deleteCompanyAssets(request, id):
    if request.user.is_authenticated:
        companyassets = CompanyAssets.objects.get(id=id)
        companyassets.delete()
        companyassets = CompanyAssets.objects.all()
        origin = Origin.objects.all()
        return render(request, "companyassets.html",{
            "companyassets": companyassets,
            "origin": origin
        })
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