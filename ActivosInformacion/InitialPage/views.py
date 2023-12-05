from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from InitialPage.models import SubtypesActives, TypesActives
from CompanyAssets.models import ClasifyActives, CompanyAssets

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, "home/home.html")
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def typesActives(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get("name")
            description = request.POST.get("description")

            typesactive = TypesActives.objects.create(
                name=name,
                description=description
            )
            typesactive.save()

            typesactives = TypesActives.objects.all()
            return render(request, "program/typesActives.html",{
                "typesactives": typesactives
            })
        else:
            typesactives = TypesActives.objects.all()
            return render(request, "program/typesActives.html",{
                "typesactives": typesactives
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def editsTypesActives(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get("name")
            description = request.POST.get("description")
            id = request.POST.get("id")
            

            typesactive = TypesActives.objects.get(pk=id)
            typesactive.name = name
            typesactive.description = description
            typesactive.save()

            typesactives = TypesActives.objects.all()
            return render(request, "program/typesActives.html",{
                "typesactives": typesactives
            })
        else:
            typesactives = TypesActives.objects.all()
            return render(request, "program/typesActives.html",{
                "typesactives": typesactives
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def deleteTypesActives(request, id):
    if request.user.is_authenticated:
        typesactive = TypesActives.objects.get(pk=id)
        typesactive.delete()
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

            typesactive = TypesActives.objects.get(id=typesactive)

            subtypeactive = SubtypesActives.objects.create(
                name=namesubtype,
                description=descriptionsubtype,
                typeActive=typesactive
            )
            subtypeactive.save()

            subtypesactives = SubtypesActives.objects.all()
            typesactives = TypesActives.objects.all()
            return render(request, "program/subtypesActives.html",{
                "subtypesactives": subtypesactives,
                "typesactives": typesactives
            })
        else:
            subtypesactives = SubtypesActives.objects.all()
            typesactives = TypesActives.objects.all()
            return render(request, "program/subtypesActives.html",{
                "subtypesactives": subtypesactives,
                "typesactives": typesactives
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def editsSubtypesActives(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            namesubtype = request.POST.get("name")
            descriptionsubtype = request.POST.get("description")
            typesactive = request.POST.get("typesactive")
            id = request.POST.get("id")

            subtypeactive = SubtypesActives.objects.get(pk=id)
            subtypeactive.name = namesubtype
            subtypeactive.description = descriptionsubtype
            subtypeactive.typeActive = TypesActives.objects.get(pk=typesactive)
            subtypeactive.save()

            subtypesactives = SubtypesActives.objects.all()
            typesactives = TypesActives.objects.all()
            return render(request, "program/subtypesActives.html",{
                "subtypesactives": subtypesactives,
                "typesactives": typesactives
            })
        else:
            subtypesactives = SubtypesActives.objects.all()
            typesactives = TypesActives.objects.all()
            return render(request, "program/subtypesActives.html",{
                "subtypesactives": subtypesactives,
                "typesactives": typesactives
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def deleteSubtypesActives(request, id):
    if request.user.is_authenticated:
        subtypeactive = SubtypesActives.objects.get(pk=id)
        subtypeactive.delete()
        subtypesactives = SubtypesActives.objects.all()
        typesactives = TypesActives.objects.all()
        return render(request, "program/subtypesActives.html",{
            "subtypesactives": subtypesactives,
            "typesactives": typesactives
        })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def clasifyactives(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            value = request.POST.get("value")
            companyassets = request.POST.get("typesactive")

            if int(value) == 1 or int(value) == 2:
                damage = "Low"
                critery = "Minor damage"

            elif int(value) == 3 or int(value) == 5:
                damage = "Medium"
                critery = "Damage of importance"

            elif int(value) == 6 or int(value) == 8:
                damage = "High"
                critery = "Serious damage"

            elif int(value) == 9:
                damage = "Very high"
                critery = "Critical damage"

            elif int(value) == 10:
                damage = "Maximum"
                critery = "Catastrophic damage"

            companyassets = CompanyAssets.objects.get(pk=companyassets)

            companyassets = ClasifyActives.objects.create(
                value=value,
                damage=damage,
                critery=critery,
                companyAssets=companyassets
            )
            companyassets.save()

            companyassets = ClasifyActives.objects.all()
            assets = CompanyAssets.objects.all()
            return render(request, "program/clasifyactives.html",{
                "companyassets": companyassets,
                "assets": assets
            })
        else:
            companyassets = ClasifyActives.objects.all()
            assets = CompanyAssets.objects.all()
            return render(request, "program/clasifyactives.html",{
                "companyassets": companyassets,
                "assets": assets
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def editsClasifyActives(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            value = request.POST.get("value")
            companyassets = request.POST.get("typesactive")
            id = request.POST.get("id")

            if int(value) == 1 or int(value) == 2:
                damage = "Low"
                critery = "Minor damage"

            elif int(value) == 3 or int(value) == 5:
                damage = "Medium"
                critery = "Damage of importance"

            elif int(value) == 6 or int(value) == 8:
                damage = "High"
                critery = "Serious damage"

            elif int(value) == 9:
                damage = "Very high"
                critery = "Critical damage"

            elif int(value) == 10:
                damage = "Maximum"
                critery = "Catastrophic damage"

            companyassets = CompanyAssets.objects.get(pk=companyassets)

            companyassets = ClasifyActives.objects.get(pk=id)
            companyassets.value = value
            companyassets.damage = damage
            companyassets.critery = critery
            companyassets.companyAssets = companyassets
            companyassets.save()

            companyassets = ClasifyActives.objects.all()
            assets = CompanyAssets.objects.all()
            return render(request, "program/clasifyactives.html",{
                "companyassets": companyassets,
                "assets": assets
            })
        else:
            companyassets = ClasifyActives.objects.all()
            assets = CompanyAssets.objects.all()
            return render(request, "program/clasifyactives.html",{
                "companyassets": companyassets,
                "assets": assets
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def deleteClasifyActives(request, id):
    if request.user.is_authenticated:
        companyassets = ClasifyActives.objects.get(pk=id)
        companyassets.delete()
        companyassets = ClasifyActives.objects.all()
        assets = CompanyAssets.objects.all()
        return render(request, "program/clasifyactives.html",{
            "companyassets": companyassets,
            "assets": assets
        })
    else:
        return HttpResponseRedirect(reverse("user:login"))