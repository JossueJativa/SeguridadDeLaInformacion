from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from CompanyAssets.models import Origin, CompanyAssets, CompanyAssetsTypes
from InitialPage.models import TypesActives, SubtypesActives

from django.http import JsonResponse

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
    
def companyType(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            companyassets = request.POST.get("companyassets")
            assettype = request.POST.get("assettype")
            subtype = request.POST.get("subtype")

            companyassets = CompanyAssets.objects.get(pk=companyassets)
            assettype = TypesActives.objects.get(pk=assettype)
            subtype = SubtypesActives.objects.get(pk=subtype)

            companytype = CompanyAssetsTypes(
                companyassets=companyassets,
                type=assettype,
                subtype=subtype
            )
            companytype.save()

            companytype = CompanyAssetsTypes.objects.all()
            companyassets = CompanyAssets.objects.all()
            types = TypesActives.objects.all()
            subtypes = SubtypesActives.objects.all()
            return render(request, "companytype.html",{
                "companytype": companytype,
                "companyassets": companyassets,
                "types": types,
                "subtypes": subtypes
            })
        else:
            companytype = CompanyAssetsTypes.objects.all()
            companyassets = CompanyAssets.objects.all()
            types = TypesActives.objects.all()
            subtypes = SubtypesActives.objects.all()
            return render(request, "companytype.html",{
                "companytype": companytype,
                "companyassets": companyassets,
                "types": types,
                "subtypes": subtypes
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def editcompanyType(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            id = request.POST.get("id")
            companyassets = request.POST.get("companyassets")
            assettype = request.POST.get("assettype")
            subtype = request.POST.get("subtype")

            companyassets = CompanyAssets.objects.get(pk=companyassets)
            assettype = TypesActives.objects.get(pk=assettype)
            subtype = SubtypesActives.objects.get(pk=subtype)

            companytype = CompanyAssetsTypes.objects.get(pk=id)
            companytype.companyassets = companyassets
            companytype.type = assettype
            companytype.subtype = subtype
            companytype.save()

            companytype = CompanyAssetsTypes.objects.all()
            companyassets = CompanyAssets.objects.all()
            types = TypesActives.objects.all()
            subtypes = SubtypesActives.objects.all()
            return render(request, "companytype.html",{
                "companytype": companytype,
                "companyassets": companyassets,
                "types": types,
                "subtypes": subtypes
            })
        else:
            companytype = CompanyAssetsTypes.objects.all()
            companyassets = CompanyAssets.objects.all()
            types = TypesActives.objects.all()
            subtypes = SubtypesActives.objects.all()
            return render(request, "companytype.html",{
                "companytype": companytype,
                "companyassets": companyassets,
                "types": types,
                "subtypes": subtypes
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def get_subtypes(request):
    asset_type_id = request.GET.get('asset_type_id')
    subtypes = SubtypesActives.objects.filter(typeActive=asset_type_id).values('id', 'name')
    return JsonResponse(list(subtypes), safe=False)