from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from CompanyAssets.models import ActivesDependecies, CompanyAssetsUnityResponsable, Origin, CompanyAssets, CompanyAssetsTypes, ResponsableUnity
from InitialPage.models import TypesActives, SubtypesActives

from django.http import JsonResponse

from Users.models import User

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
    
def deletecompanyType(request, id):
    if request.user.is_authenticated:
        companytype = CompanyAssetsTypes.objects.get(id=id)
        companytype.delete()
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

def responsableunity(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get("name")
            description = request.POST.get("description")
            responsableunity = ResponsableUnity(name=name, description=description)
            responsableunity.save()
            responsableunity = ResponsableUnity.objects.all()
            return render(request, "responsableunity.html",{
                "responsableunity": responsableunity
            })
        else:
            responsableunity = ResponsableUnity.objects.all()
            return render(request, "responsableunity.html",{
                "responsableunity": responsableunity
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def editresponsableunity(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            id = request.POST.get("id")
            name = request.POST.get("name")
            description = request.POST.get("description")
            responsableunity = ResponsableUnity.objects.get(pk=id)
            responsableunity.name = name
            responsableunity.description = description
            responsableunity.save()
            responsableunity = ResponsableUnity.objects.all()
            return render(request, "responsableunity.html",{
                "responsableunity": responsableunity
            })
        else:
            responsableunity = ResponsableUnity.objects.all()
            return render(request, "responsableunity.html",{
                "responsableunity": responsableunity
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def deleteresponsableunity(request, id):
    if request.user.is_authenticated:
        responsableunity = ResponsableUnity.objects.get(id=id)
        responsableunity.delete()
        responsableunity = ResponsableUnity.objects.all()
        return render(request, "responsableunity.html",{
            "responsableunity": responsableunity
        })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def companyunity(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            companyassets = request.POST.get("companyassets")
            responsableunity = request.POST.get("responsableunity")

            companyassets = CompanyAssets.objects.get(pk=companyassets)
            responsableunity = ResponsableUnity.objects.get(pk=responsableunity)

            companyunity = CompanyAssetsUnityResponsable(
                companyassets=companyassets,
                responsableunity=responsableunity
            )
            companyunity.save()

            companyunity = CompanyAssetsUnityResponsable.objects.all()
            companyassets = CompanyAssets.objects.all()
            responsableunity = ResponsableUnity.objects.all()
            return render(request, "companyunity.html",{
                "companyunity": companyunity,
                "companyassets": companyassets,
                "responsableunity": responsableunity
            })
        else:
            companyunity = CompanyAssetsUnityResponsable.objects.all()
            companyassets = CompanyAssets.objects.all()
            responsableunity = ResponsableUnity.objects.all()
            return render(request, "companyunity.html",{
                "companyunity": companyunity,
                "companyassets": companyassets,
                "responsableunity": responsableunity
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def editcompanyunity(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            id = request.POST.get("id")
            companyassets = request.POST.get("companyassets")
            responsableunity = request.POST.get("responsableunity")

            companyassets = CompanyAssets.objects.get(pk=companyassets)
            responsableunity = ResponsableUnity.objects.get(pk=responsableunity)

            companyunity = CompanyAssetsUnityResponsable.objects.get(pk=id)
            companyunity.companyassets = companyassets
            companyunity.responsableunity = responsableunity
            companyunity.save()

            companyunity = CompanyAssetsUnityResponsable.objects.all()
            companyassets = CompanyAssets.objects.all()
            responsableunity = ResponsableUnity.objects.all()
            return render(request, "companyunity.html",{
                "companyunity": companyunity,
                "companyassets": companyassets,
                "responsableunity": responsableunity
            })
        else:
            companyunity = CompanyAssetsUnityResponsable.objects.all()
            companyassets = CompanyAssets.objects.all()
            responsableunity = ResponsableUnity.objects.all()
            return render(request, "companyunity.html",{
                "companyunity": companyunity,
                "companyassets": companyassets,
                "responsableunity": responsableunity
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def deletecompanyunity(request, id):
    if request.user.is_authenticated:
        companyunity = CompanyAssetsUnityResponsable.objects.get(id=id)
        companyunity.delete()
        companyunity = CompanyAssetsUnityResponsable.objects.all()
        companyassets = CompanyAssets.objects.all()
        responsableunity = ResponsableUnity.objects.all()
        return render(request, "companyunity.html",{
            "companyunity": companyunity,
            "companyassets": companyassets,
            "responsableunity": responsableunity
        })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def dependentassets(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            dependencypercentage = request.POST.get("dependencypercentage")
            descriptiondependency = request.POST.get("descriptiondependency")
            Interviewed = request.POST.get("Interviewed")
            companyassetsindependent = request.POST.get("companyassetsindependent")
            companyassetsdependent = request.POST.get("companyassetsdependent")

            Interviewed = User.objects.get(pk=Interviewed)
            companyassetsindependent = CompanyAssets.objects.get(pk=companyassetsindependent)
            companyassetsdependent = CompanyAssets.objects.get(pk=companyassetsdependent)

            dependentassets = ActivesDependecies(
                dependencypercentage=dependencypercentage,
                descriptiondependency=descriptiondependency,
                Interviewed=Interviewed,
                companyassetsindependent=companyassetsindependent,
                companyassetsdependent=companyassetsdependent
            )
            dependentassets.save()

            dependentassets = ActivesDependecies.objects.all()
            companyassets = CompanyAssets.objects.all()
            users = User.objects.all()
            return render(request, "dependencesassets.html",{
                "dependentassets": dependentassets,
                "companyassets": companyassets,
                "users": users
            })
        else:
            dependentassets = ActivesDependecies.objects.all()
            companyassets = CompanyAssets.objects.all()
            users = User.objects.all()
            return render(request, "dependencesassets.html",{
                "dependentassets": dependentassets,
                "companyassets": companyassets,
                "users": users
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def editdependentassets(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            id = request.POST.get("id")
            dependencypercentage = request.POST.get("dependencypercentage")
            descriptiondependency = request.POST.get("descriptiondependency")
            Interviewed = request.POST.get("Interviewed")
            companyassetsindependent = request.POST.get("companyassetsindependent")
            companyassetsdependent = request.POST.get("companyassetsdependent")

            Interviewed = User.objects.get(pk=Interviewed)
            companyassetsindependent = CompanyAssets.objects.get(pk=companyassetsindependent)
            companyassetsdependent = CompanyAssets.objects.get(pk=companyassetsdependent)

            dependentassets = ActivesDependecies.objects.get(pk=id)
            dependentassets.dependencypercentage = dependencypercentage
            dependentassets.descriptiondependency = descriptiondependency
            dependentassets.Interviewed = Interviewed
            dependentassets.companyassetsindependent = companyassetsindependent
            dependentassets.companyassetsdependent = companyassetsdependent
            dependentassets.save()

            dependentassets = ActivesDependecies.objects.all()
            companyassets = CompanyAssets.objects.all()
            users = User.objects.all()
            return render(request, "dependencesassets.html",{
                "dependentassets": dependentassets,
                "companyassets": companyassets,
                "users": users
            })
        else:
            dependentassets = ActivesDependecies.objects.all()
            companyassets = CompanyAssets.objects.all()
            users = User.objects.all()
            return render(request, "dependencesassets.html",{
                "dependentassets": dependentassets,
                "companyassets": companyassets,
                "users": users
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def deletedependentassets(request, id):
    if request.user.is_authenticated:
        dependentassets = ActivesDependecies.objects.get(id=id)
        dependentassets.delete()
        dependentassets = ActivesDependecies.objects.all()
        companyassets = CompanyAssets.objects.all()
        users = User.objects.all()
        return render(request, "dependencesassets.html",{
            "dependentassets": dependentassets,
            "companyassets": companyassets,
            "users": users
        })
    else:
        return HttpResponseRedirect(reverse("user:login"))