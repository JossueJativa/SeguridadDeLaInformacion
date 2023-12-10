from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from InitialPage.models import Departments, Assets, AssetsDependence, AssetsValue, TypeAssets, SubtypeAssets
from Users.models import User, Workload

# Create your views here.
def enterAsset(request):
    if request.user.is_authenticated:
        # Obtener todos los departamentos sin nombres duplicados
        departmentsName = Departments.objects.values('name').distinct()

        # Crear id para cada departamento
        for department in departmentsName:
            department['id'] = Departments.objects.filter(name=department['name']).first().id

        if request.method == "POST":
            # Informacion inicial
            origin = request.POST.get("origin")
            code = request.POST.get("code")
            name = request.POST.get("name")
            type = request.POST.get("type")
            subtype = request.POST.get("subtype")
            responsableArea = request.POST.get("responsableArea")
            responsablePerson = request.POST.get("responsablePerson")
            ubicationType = request.POST.get("ubicationType")
            ubication = request.POST.get("ubication")
            quantity = request.POST.get("quantity")
            characteristic = request.POST.get("characteristic")

            # Verificacion de toggles
            state = request.POST.get("state")
            state2 = request.POST.get("state2")

            #Guardar el activo
            try:
                asset = Assets(
                    code = code,
                    origin = origin,
                    name = name,
                    ubicationType = ubicationType,
                    ubication = ubication,
                    quantity = quantity,
                    characteristic = characteristic,
                    type = TypeAssets.objects.get(pk=type),
                    responsableArea = Departments.objects.get(pk=responsableArea),
                    responsableUser = User.objects.get(pk=responsablePerson)
                )
                asset.save()
            except Exception as e:
                return render(request, "home/enterAsset.html",{
                    "Departments": departmentsName,
                    # Parte principal
                    "origin": origin,
                    "code": code,
                    "name": name,
                    "type": type,
                    "subtype": subtype,
                    "responsableArea": responsableArea,
                    "responsablePerson": responsablePerson,
                    "ubicationType": ubicationType,
                    "ubication": ubication,
                    "quantity": quantity,
                    "characteristic": characteristic,
                    "message": f"Error al ingresar el activo {e}"
                })
            
            if state == "on":
                #Informacion de dependencias
                dependency = request.POST.get("dependency")
                descriptionDependency = request.POST.get("descriptionDependency")
                responsableUser = request.POST.get("responsableUser")
                dependsOf = request.POST.get("dependsOf")

                if dependency == "" or dependency == None:
                    return render(request, "home/enterAsset.html",{
                        "Departments": departmentsName,
                        # Parte principal
                        "origin": origin,
                        "code": code,
                        "name": name,
                        "type": type,
                        "subtype": subtype,
                        "responsableArea": responsableArea,
                        "responsablePerson": responsablePerson,
                        "ubicationType": ubicationType,
                        "ubication": ubication,
                        "quantity": quantity,
                        "characteristic": characteristic,
                        # Activacion del toggle
                        "state": state,
                        "descriptionDependency": descriptionDependency,
                        "responsableUser": responsableUser,
                        "dependsOf": dependsOf,
                        "message": "Seleccione la dependencia",
                    })
                
                if descriptionDependency == "" or descriptionDependency == None:
                    return render(request, "home/enterAsset.html",{
                        "Departments": departmentsName,
                        # Parte principal
                        "origin": origin,
                        "code": code,
                        "name": name,
                        "type": type,
                        "subtype": subtype,
                        "responsableArea": responsableArea,
                        "responsablePerson": responsablePerson,
                        "ubicationType": ubicationType,
                        "ubication": ubication,
                        "quantity": quantity,
                        "characteristic": characteristic,
                        # Activacion del toggle
                        "state": state,
                        "dependency": dependency,
                        "responsableUser": responsableUser,
                        "dependsOf": dependsOf,
                        "message": "Ingrese la descripción de la dependencia",
                    })
                
                if responsableUser == "" or responsableUser == None:
                    return render(request, "home/enterAsset.html",{
                        "Departments": departmentsName,
                        # Parte principal
                        "origin": origin,
                        "code": code,
                        "name": name,
                        "type": type,
                        "subtype": subtype,
                        "responsableArea": responsableArea,
                        "responsablePerson": responsablePerson,
                        "ubicationType": ubicationType,
                        "ubication": ubication,
                        "quantity": quantity,
                        "characteristic": characteristic,
                        # Activacion del toggle
                        "state": state,
                        "dependency": dependency,
                        "descriptionDependency": descriptionDependency,
                        "dependsOf": dependsOf,
                        "message": "Seleccione el responsable del activo"
                    })
                
                if dependsOf == "" or dependsOf == None:
                    return render(request, "home/enterAsset.html",{
                        "Departments": departmentsName,
                        # Parte principal
                        "origin": origin,
                        "code": code,
                        "name": name,
                        "type": type,
                        "subtype": subtype,
                        "responsableArea": responsableArea,
                        "responsablePerson": responsablePerson,
                        "ubicationType": ubicationType,
                        "ubication": ubication,
                        "quantity": quantity,
                        "characteristic": characteristic,
                        # Activacion del toggle 1
                        "state": state,
                        "dependency": dependency,
                        "descriptionDependency": descriptionDependency,
                        "responsableUser": responsableUser,
                        "message": "Seleccione de que depende"
                    })
                
                responsableUser = User.objects.get(pk=responsableUser)
                dependsOf = Assets.objects.get(pk=dependsOf)

                try:
                    assetDependence = AssetsDependence(
                        percentaje = dependency,
                        asset = asset,
                        responsableUser = responsableUser,
                        assetDepend = dependsOf
                    )
                    assetDependence.save()
                except Exception as e:
                    return render(request, "home/enterAsset.html",{
                        "Departments": departmentsName,
                        # Parte principal
                        "origin": origin,
                        "code": code,
                        "name": name,
                        "type": type,
                        "subtype": subtype,
                        "responsableArea": responsableArea,
                        "responsablePerson": responsablePerson,
                        "ubicationType": ubicationType,
                        "ubication": ubication,
                        "quantity": quantity,
                        "characteristic": characteristic,
                        # Activacion del toggle 1
                        "state": state,
                        "dependency": dependency,
                        "descriptionDependency": descriptionDependency,
                        "responsableUser": responsableUser,
                        "dependsOf": dependsOf,
                        "message": f"Error al ingresar la dependencia {e}"
                    })

            if state2 == "on":
                # Informacion de valoracion
                valorationDimention = request.POST.get("valorationDimention")
                valorationAssing = request.POST.get("valorationAssing")
                cualitative = request.POST.get("cualitative")
                descriptionValue = request.POST.get("descriptionValue")
                
                if valorationDimention == "" or valorationDimention == None:
                    return render(request, "home/enterAsset.html",{
                        "Departments": departmentsName,
                        # Parte principal
                        "origin": origin,
                        "code": code,
                        "name": name,
                        "type": type,
                        "subtype": subtype,
                        "responsableArea": responsableArea,
                        "responsablePerson": responsablePerson,
                        "ubicationType": ubicationType,
                        "ubication": ubication,
                        "quantity": quantity,
                        "characteristic": characteristic,
                        "message": "Seleccione la dimensión de valoración"
                    })
                
                if valorationAssing == "" or valorationAssing == None:
                    return render(request, "home/enterAsset.html",{
                        "Departments": departmentsName,
                        # Parte principal
                        "origin": origin,
                        "code": code,
                        "name": name,
                        "type": type,
                        "subtype": subtype,
                        "responsableArea": responsableArea,
                        "responsablePerson": responsablePerson,
                        "ubicationType": ubicationType,
                        "ubication": ubication,
                        "quantity": quantity,
                        "characteristic": characteristic,
                        "message": "Seleccione la valoración"
                    })
                
                try:
                    assetValue = AssetsValue(
                        cuantityValue = valorationAssing,
                        cualityValue = cualitative,
                        description = descriptionValue,
                        dimentionValue = valorationDimention,
                        asset = asset
                    )
                    assetValue.save()
                except Exception as e:
                    return render(request, "home/enterAsset.html",{
                        "Departments": departmentsName,
                        # Parte principal
                        "origin": origin,
                        "code": code,
                        "name": name,
                        "type": type,
                        "subtype": subtype,
                        "responsableArea": responsableArea,
                        "responsablePerson": responsablePerson,
                        "ubicationType": ubicationType,
                        "ubication": ubication,
                        "quantity": quantity,
                        "characteristic": characteristic,
                        "message": f"Error al ingresar la valoración {e}"
                    })
                
                try:
                    # ver si los otros campos estan llenos para guardarlos o no
                    # Primeros campos
                    valorationDimention2 = request.POST.get("valorationDimention2")
                    valorationAssing2 = request.POST.get("valorationAssing2")
                    subtype= SubtypeAssets.objects.get(pk=subtype)
                    if valorationDimention2 != None or valorationDimention2 != "" or valorationAssing2 != None or valorationAssing2 != "":
                        descriptionValue2 = request.POST.get("descriptionValue2")
                        cualitative2 = request.POST.get("cualitative2")
                        
                        try:
                            assetValue = AssetsValue(
                                cuantityValue = valorationAssing2,
                                cualityValue = cualitative2,
                                description = descriptionValue2,
                                dimentionValue = valorationDimention2,
                                asset = asset,
                            )
                            assetValue.save()
                        except Exception as e:
                            return render(request, "home/enterAsset.html",{
                                "Departments": departmentsName,
                                # Parte principal
                                "origin": origin,
                                "code": code,
                                "name": name,
                                "type": type,
                                "subtype": subtype,
                                "responsableArea": responsableArea,
                                "responsablePerson": responsablePerson,
                                "ubicationType": ubicationType,
                                "ubication": ubication,
                                "quantity": quantity,
                                "characteristic": characteristic,
                            })
                except Exception as e:
                    pass
                    
                try:
                    # ver si los otros campos estan llenos para guardarlos o no
                    # Segundos campos
                    valorationDimention3 = request.POST.get("valorationDimention3")
                    valorationAssing3 = request.POST.get("valorationAssing3")

                    if valorationDimention3 != None or valorationDimention3 != "" or valorationAssing3 != None or valorationAssing3 != "":
                        descriptionValue3 = request.POST.get("descriptionValue3")
                        cualitative3 = request.POST.get("cualitative3")
                        
                        try:
                            assetValue = AssetsValue(
                                cuantityValue = valorationAssing3,
                                cualityValue = cualitative3,
                                description = descriptionValue3,
                                dimentionValue = valorationDimention3,
                                asset = asset
                            )
                            assetValue.save()
                        except Exception as e:
                            return render(request, "home/enterAsset.html",{
                                "Departments": departmentsName,
                                # Parte principal
                                "origin": origin,
                                "code": code,
                                "name": name,
                                "type": type,
                                "subtype": subtype,
                                "responsableArea": responsableArea,
                                "responsablePerson": responsablePerson,
                                "ubicationType": ubicationType,
                                "ubication": ubication,
                                "quantity": quantity,
                                "characteristic": characteristic,
                                "responsableUser": responsableUser
                            })
                except Exception as e:
                    pass

                try:
                    # ver si los otros campos estan llenos para guardarlos o no
                    # Terceros campos
                    valorationDimention4 = request.POST.get("valorationDimention4")
                    valorationAssing4 = request.POST.get("valorationAssing4")

                    if valorationDimention4 != None or valorationDimention4 != "" or valorationAssing4 != None or valorationAssing4 != "":
                        descriptionValue4 = request.POST.get("descriptionValue4")
                        cualitative4 = request.POST.get("cualitative4")
                        
                        try:
                            assetValue = AssetsValue(
                                cuantityValue = valorationAssing4,
                                cualityValue = cualitative4,
                                description = descriptionValue4,
                                dimentionValue = valorationDimention4,
                                asset = asset
                            )
                            assetValue.save()
                        except Exception as e:
                            return render(request, "home/enterAsset.html",{
                                "Departments": departmentsName,
                                # Parte principal
                                "origin": origin,
                                "code": code,
                                "name": name,
                                "type": type,
                                "subtype": subtype,
                                "responsableArea": responsableArea,
                                "responsablePerson": responsablePerson,
                                "ubicationType": ubicationType,
                                "ubication": ubication,
                                "quantity": quantity,
                                "characteristic": characteristic,
                                "responsableUser": responsableUser
                            })
                except Exception as e:
                    pass

                try:
                    # ver si los otros campos estan llenos para guardarlos o no
                    # Cuartos campos
                    valorationDimention5 = request.POST.get("valorationDimention5")
                    valorationAssing5 = request.POST.get("valorationAssing5")

                    if valorationDimention5 != None or valorationDimention5 != "" or valorationAssing5 != None or valorationAssing5 != "":
                        descriptionValue5 = request.POST.get("descriptionValue4")
                        cualitative5 = request.POST.get("cualitative4")
                        
                        try:
                            assetValue = AssetsValue(
                                cuantityValue = valorationAssing5,
                                cualityValue = cualitative5,
                                description = descriptionValue5,
                                dimentionValue = valorationDimention5,
                                asset = asset
                            )
                            assetValue.save()
                        except Exception as e:
                            return render(request, "home/enterAsset.html",{
                                "Departments": departmentsName,
                                # Parte principal
                                "origin": origin,
                                "code": code,
                                "name": name,
                                "type": type,
                                "subtype": subtype,
                                "responsableArea": responsableArea,
                                "responsablePerson": responsablePerson,
                                "ubicationType": ubicationType,
                                "ubication": ubication,
                                "quantity": quantity,
                                "characteristic": characteristic,
                                "responsableUser": responsableUser,
                            })
                except Exception as e:
                    pass

            return render(request, "tables/assets.html",{
                "DependentAssets": AssetsDependence.objects.all(),
                "AssetsValue": AssetsValue.objects.all()
            })
        else:
            return render(request, "home/enterAsset.html",{
                "Departments": departmentsName,
                "Users": User.objects.all(),
                "Assets": Assets.objects.all(),
                "TypeAssets": TypeAssets.objects.all(),
                "SubtypeAssets": SubtypeAssets.objects.all()
            })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))

def tableAssets(request):
    if request.user.is_authenticated:
        return render(request, "tables/assets.html",{
            "DependentAssets": AssetsDependence.objects.all(),
            "AssetsValue": AssetsValue.objects.all()
        })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))

def editTableAssets(request):
    if request.method == "POST":
        # Obtener todos los departamentos sin nombres duplicados
        departmentsName = Departments.objects.values('name').distinct()

        # Crear id para cada departamento
        for department in departmentsName:
            department['id'] = Departments.objects.filter(name=department['name']).first().id

        if request.method == "POST":
            # Informacion inicial
            assetValueID = request.POST.get("assetValueID")
            assetId = request.POST.get("assetId")
            origin = request.POST.get("origin")
            code = request.POST.get("code")
            name = request.POST.get("name")
            type = request.POST.get("type")
            subtype = request.POST.get("subtype")
            responsableArea = request.POST.get("responsableArea")
            responsablePerson = request.POST.get("responsablePerson")
            ubicationType = request.POST.get("ubicationType")
            ubication = request.POST.get("ubication")
            quantity = request.POST.get("quantity")
            characteristic = request.POST.get("characteristic")

            # Verificacion de toggles
            state2 = request.POST.get("state2")

            asset = Assets.objects.get(pk=assetId)

        if state2 == "on":
            # Informacion de valoracion
            valorationDimention = request.POST.get("valorationDimention")
            valorationAssing = request.POST.get("valorationAssing")
            cualitative = request.POST.get("cualitative")
            descriptionValue = request.POST.get("descriptionValue")
            
            if valorationDimention == "" or valorationDimention == None:
                return render(request, "home/enterAsset.html",{
                    "Departments": departmentsName,
                    # Parte principal
                    "origin": origin,
                    "code": code,
                    "name": name,
                    "type": type,
                    "subtype": subtype,
                    "responsableArea": responsableArea,
                    "responsablePerson": responsablePerson,
                    "ubicationType": ubicationType,
                    "ubication": ubication,
                    "quantity": quantity,
                    "characteristic": characteristic,
                    "message": "Seleccione la dimensión de valoración"
                })
            
            if valorationAssing == "" or valorationAssing == None:
                return render(request, "home/enterAsset.html",{
                    "Departments": departmentsName,
                    # Parte principal
                    "origin": origin,
                    "code": code,
                    "name": name,
                    "type": type,
                    "subtype": subtype,
                    "responsableArea": responsableArea,
                    "responsablePerson": responsablePerson,
                    "ubicationType": ubicationType,
                    "ubication": ubication,
                    "quantity": quantity,
                    "characteristic": characteristic,
                    "message": "Seleccione la valoración"
                })
            
            try:
                # Actualizar asset value
                AssetsValue.objects.filter(pk=assetValueID).update(
                    cuantityValue = valorationAssing,
                    cualityValue = cualitative,
                    description = descriptionValue,
                    dimentionValue = valorationDimention,
                    asset = asset
                )
            except Exception as e:
                return render(request, "home/enterAsset.html",{
                    "Departments": departmentsName,
                    # Parte principal
                    "origin": origin,
                    "code": code,
                    "name": name,
                    "type": type,
                    "subtype": subtype,
                    "responsableArea": responsableArea,
                    "responsablePerson": responsablePerson,
                    "ubicationType": ubicationType,
                    "ubication": ubication,
                    "quantity": quantity,
                    "characteristic": characteristic,
                    "message": f"Error al ingresar la valoración {e}"
                })
        # Actializar campos
        try:
            Assets.objects.filter(pk=asset.id).update(
                code = code,
                origin = origin,
                name = name,
                ubicationType = ubicationType,
                ubication = ubication,
                quantity = quantity,
                characteristic = characteristic,
                type = TypeAssets.objects.get(pk=type),
                responsableArea = Departments.objects.get(pk=responsableArea),
                responsableUser = User.objects.get(pk=responsablePerson)
            )
        except Exception as e:
            return render(request, "home/enterAsset.html",{
                "Departments": departmentsName,
                # Parte principal
                "origin": origin,
                "code": code,
                "name": name,
                "type": type,
                "subtype": subtype,
                "responsableArea": responsableArea,
                "responsablePerson": responsablePerson,
                "ubicationType": ubicationType,
                "ubication": ubication,
                "quantity": quantity,
                "characteristic": characteristic,
                "message": f"Error al ingresar el activo {e}"
            })

        return render(request, "tables/assets.html",{
            "DependentAssets": AssetsDependence.objects.all(),
            "AssetsValue": AssetsValue.objects.all()
        })   

def deleteTableAssets(request, id):
    if request.user.is_authenticated:
        try:
            asset = Assets.objects.get(pk=id)
            # Eliminar las dependencias
            assetsDependence = AssetsDependence.objects.filter(assetDepend=asset)
            for assetDependence in assetsDependence:
                assetDependence.delete()

            # Eliminar los valores
            assetsValue = AssetsValue.objects.filter(asset=asset)
            for assetValue in assetsValue:
                assetValue.delete()
            asset.delete()
        except Exception as e:
            return render(request, "tables/assets.html",{
                "DependentAssets": AssetsDependence.objects.all(),
                "AssetsValue": AssetsValue.objects.all(),
                "message": f"Error al eliminar el activo {e}"
            })
        
        return render(request, "tables/assets.html",{
            "DependentAssets": AssetsDependence.objects.all(),
            "AssetsValue": AssetsValue.objects.all(),
        })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))

def enterUsers(request):
    if request.user.is_authenticated:
        # Obtener todos los departamentos sin nombres duplicados
        departmentsName = Departments.objects.values('name').distinct()

        # Crear id para cada departamento
        for department in departmentsName:
            department['id'] = Departments.objects.filter(name=department['name']).first().id

        if request.method == "POST":
            firstname = request.POST.get("firstname")
            lastname = request.POST.get("lastname")
            email = request.POST.get("email")
            celular = request.POST.get("phone")
            password = request.POST.get("password")
            confirm = request.POST.get("confirm")
            userDepartment = request.POST.get("userDepartment")
            workload = request.POST.get("workload")

            if firstname == "" or firstname == None:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": departmentsName,
                    "message": "Ingrese el nombre del usuario"
                })
            
            if lastname == "" or lastname == None:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": departmentsName,
                    "message": "Ingrese el apellido del usuario"
                })
            
            if email == "" or email == None:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": departmentsName,
                    "message": "Ingrese el correo del usuario"
                })
            
            if celular == "" or celular == None:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": departmentsName,
                    "message": "Ingrese la identidad del usuario"
                })
            
            if password == "" or password == None:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": departmentsName,
                    "message": "Ingrese la contraseña del usuario"
                })
            
            if confirm == "" or confirm == None:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": departmentsName,
                    "message": "Confirme la contraseña del usuario"
                })
            
            if userDepartment == "" or userDepartment == None:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": departmentsName,
                    "message": "Seleccione el departamento del usuario"
                })
            
            if workload == "" or workload == None:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": departmentsName,
                    "message": "Seleccione la carga de trabajo del usuario"
                })
            
            if password != confirm:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": departmentsName,
                    "message": "Las contraseñas no coinciden"
                })
            
            workload = Workload.objects.get(pk=workload)
            userDepartment = Departments.objects.get(pk=userDepartment)

            try:
                department = Departments(
                    name = userDepartment.name,
                    description = userDepartment.description,
                    workload = workload
                )
                department.save()
            except Exception as e:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": departmentsName,
                    "message": f"Error al ingresar el departamento {e}"
                })
            
            try:
                idlastUser = User.objects.last()
            except:
                idlastUser = 1
            
            username = f"{firstname}.{lastname}.{idlastUser.id}"

            try:
                user = User(
                    first_name = firstname,
                    last_name = lastname,
                    email = email,
                    celular = celular,
                    password = password,
                    workload = workload,
                    username= username,
                    department = department.name
                )
                user.save()
            except Exception as e:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": departmentsName,
                    "message": f"Error al ingresar el usuario {e}"
                })
            
            return render(request, "tables/users.html",{
                "Users": User.objects.all(),
            })
        return render(request, "home/enterUsers.html",{
            "Workloads": Workload.objects.all(),
            "Departments": departmentsName
        })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def tableusers(request):
    if request.user.is_authenticated:
        return render(request, "tables/users.html",{
            "Users": User.objects.all(),
            "Departments": Departments.objects.all()
        })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def deleteTableUsers(request, id):
    if request.user.is_authenticated:
        try:
            user = User.objects.get(pk=id)
            user.delete()
        except Exception as e:
            return render(request, "tables/users.html",{
                "Users": User.objects.all(),
                "message": f"Error al eliminar el usuario {e}"
            })
        
        return render(request, "tables/users.html",{
            "Users": User.objects.all(),
        })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))

def editTableUsers(request):
    if request.method == "POST":
        userId = request.POST.get("userId")
        firstname = request.POST.get("userFirstName")
        lastname = request.POST.get("userLastName")
        username = request.POST.get("userUsername")
        email = request.POST.get("userEmail")
        celular = request.POST.get("userCelular")
        userDepartment = request.POST.get("userDepartment")
        workload = request.POST.get("userWorkload")

        if firstname == "" or firstname == None:
            return render(request, "home/users.html",{
                "Workloads": Workload.objects.all(),
                "Departments": Departments.objects.all(),
                "message": "Ingrese el nombre del usuario"
            })
        
        if lastname == "" or lastname == None:
            return render(request, "home/users.html",{
                "Workloads": Workload.objects.all(),
                "Departments": Departments.objects.all(),
                "message": "Ingrese el apellido del usuario"
            })
        
        if email == "" or email == None:
            return render(request, "home/users.html",{
                "Workloads": Workload.objects.all(),
                "Departments": Departments.objects.all(),
                "message": "Ingrese el correo del usuario"
            })
        
        if celular == "" or celular == None:
            return render(request, "home/users.html",{
                "Workloads": Workload.objects.all(),
                "Departments": Departments.objects.all(),
                "message": "Ingrese la identidad del usuario"
            })
        
        if userDepartment == "" or userDepartment == None:
            return render(request, "home/users.html",{
                "Workloads": Workload.objects.all(),
                "Departments": Departments.objects.all(),
                "message": "Seleccione el departamento del usuario"
            })
        
        if workload == "" or workload == None:
            return render(request, "home/users.html",{
                "Workloads": Workload.objects.all(),
                "Departments": Departments.objects.all(),
                "message": "Seleccione la carga de trabajo del usuario"
            })
        
        workload = Workload.objects.get(pk=workload)
        userDepartment = Departments.objects.get(pk=userDepartment)
        try:
            department = Departments(
                name = userDepartment.name,
                description = userDepartment.description,
                workload = workload
            )
            department.save()
        except Exception as e:
            return render(request, "home/users.html",{
                "Workloads": Workload.objects.all(),
                "Departments": Departments.objects.all(),
                "message": f"Error al ingresar el departamento {e}"
            })
        
        try:
            User.objects.filter(pk=userId).update(
                first_name = firstname,
                last_name = lastname,
                username=username,
                email = email,
                celular = celular,
                workload = workload,
                department = department.name
            )
        except Exception as e:
            return render(request, "home/users.html",{
                "Workloads": Workload.objects.all(),
                "Departments": Departments.objects.all(),
                "message": f"Error al ingresar el usuario {e}"
            })
        
        return render(request, "tables/users.html",{
            "Users": User.objects.all(),
        })
    else:
        return render(request, "home/enterUsers.html",{
            "Workloads": Workload.objects.all(),
            "Departments": Departments.objects.all()
        })

def enterDepartment(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            departmentName = request.POST.get("departmentName")
            description = request.POST.get("description")
            workload = request.POST.get("workload")

            if departmentName == "" or departmentName == None:
                return render(request, "home/enterDepartment.html",{
                    "Workloads": Workload.objects.all(),
                    "message": "Ingrese el nombre del departamento"
                })
            
            if description == "" or description == None:
                return render(request, "home/enterDepartment.html",{
                    "Workloads": Workload.objects.all(),
                    "message": "Ingrese la descripción del departamento"
                })
            
            if workload == "" or workload == None:
                return render(request, "home/enterDepartment.html",{
                    "Workloads": Workload.objects.all(),
                    "message": "Ingrese la carga de trabajo del departamento"
                })

            workload = Workload.objects.get(pk=workload)

            try:
                department = Departments(
                    name = departmentName,
                    description = description,
                    workload = workload
                )
                department.save()
            except Exception as e:
                return render(request, "home/enterDepartment.html",{
                    "Workloads": Workload.objects.all(),
                    "message": f"Error al ingresar el departamento {e}"
                })
            
            return render(request, "tables/departaments.html",{
                "Departments": Departments.objects.all(),
            })
        else:
            return render(request, "home/enterDepartment.html",{
                "Workloads": Workload.objects.all()
            })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def tabledepartments(request):
    if request.user.is_authenticated:
        return render(request, "tables/departaments.html",{
            "Departments": Departments.objects.all()
        })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def deleteTableDepartments(request, id):
    if request.user.is_authenticated:
        try:
            department = Departments.objects.get(pk=id)
            department.delete()
        except Exception as e:
            return render(request, "tables/departaments.html",{
                "Departments": Departments.objects.all(),
                "message": f"Error al eliminar el departamento {e}"
            })
        
        return render(request, "tables/departaments.html",{
            "Departments": Departments.objects.all(),
        })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))

def editTableDepartments(request):
    if request.method == "POST":
        departmentId = request.POST.get("departmentId")
        departmentName = request.POST.get("departmentName")
        description = request.POST.get("description")
        workload = request.POST.get("workload")

        if departmentName == "" or departmentName == None:
            return render(request, "home/enterDepartment.html",{
                "Workloads": Workload.objects.all(),
                "message": "Ingrese el nombre del departamento"
            })
        
        if description == "" or description == None:
            return render(request, "home/enterDepartment.html",{
                "Workloads": Workload.objects.all(),
                "message": "Ingrese la descripción del departamento"
            })
        
        if workload == "" or workload == None:
            return render(request, "home/enterDepartment.html",{
                "Workloads": Workload.objects.all(),
                "message": "Ingrese la carga de trabajo del departamento"
            })

        workload = Workload.objects.get(pk=workload)

        try:
            Departments.objects.filter(pk=departmentId).update(
                name = departmentName,
                description = description,
                workload = workload
            )
        except Exception as e:
            return render(request, "home/enterDepartment.html",{
                "Workloads": Workload.objects.all(),
                "message": f"Error al ingresar el departamento {e}"
            })
        
        return render(request, "tables/departaments.html",{
            "Departments": Departments.objects.all(),
        })
    else:
        return render(request, "home/enterDepartment.html",{
            "Workloads": Workload.objects.all()
        })

def get_subtypes(request, type_id):
    subtypes = SubtypeAssets.objects.filter(type_id=type_id).values('id', 'name')
    return JsonResponse(list(subtypes), safe=False)

def get_workloads(request):
    workloads = Workload.objects.all().values('id', 'name')
    return JsonResponse(list(workloads), safe=False)

def get_departments(request):
    departmentsName = Departments.objects.values('name').distinct()

    # Crear id para cada departamento
    for department in departmentsName:
        department['id'] = Departments.objects.filter(name=department['name']).first().id
    return JsonResponse(list(departmentsName), safe=False)

def get_dependentAssets(request):
    dependentAssets = AssetsDependence.objects.all().values('id', 'asset', 'percentaje', 'assetDepend')
    return JsonResponse(list(dependentAssets), safe=False)

def get_assets(request):
    assets = Assets.objects.all().values('id', 'name')
    return JsonResponse(list(assets), safe=False)

def get_types(request):
    types = TypeAssets.objects.all().values('id', 'name')
    return JsonResponse(list(types), safe=False)

def get_subtypes2(request):
    subtypes = SubtypeAssets.objects.all().values('id', 'name')
    return JsonResponse(list(subtypes), safe=False)

def get_users(request):
    users = User.objects.all().values('id', 'username', 'first_name', 'last_name')
    return JsonResponse(list(users), safe=False)