from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate

from InitialPage.models import Departments, Assets, AssetsDependence, AssetsValue, TypeAssets, SubtypeAssets, Risk, AssetsRisk, RiskType, Safeguards, SafeguardsRisk, SafeguardsTypes
from Users.models import User, Workload

# Create your views here.
def generate_asset_code():
    # Obtén el último código almacenado en la base de datos
    last_asset = Assets.objects.last()

    if last_asset:
        last_code = last_asset.code
        prefix = last_code[:-4]  # Obtiene los primeros dos caracteres (por ejemplo, 'AA')
        number = int(last_code[-4:]) + 1  # Obtiene los últimos cuatro caracteres y les suma 1
        if number > 9999:
            # Si el número excede 9999, cambia a la siguiente combinación de letras
            prefix = chr(ord(prefix[0]) + 1) + prefix[1]  # Cambia la primera letra a la siguiente en el alfabeto
            number = 1  # Reinicia el número a 1

        new_code = f"{prefix}{number:04d}"  # Formatea el nuevo código
    else:
        # Si no hay ningún registro en la base de datos, comienza desde el principio
        new_code = "AA0001"

    return new_code

def enterAsset(request):
    if request.user.is_authenticated:
        departmentsName = Departments.objects.values('name').distinct()

        # Crear id para cada departamento
        for department in departmentsName:
            department['id'] = Departments.objects.filter(name=department['name']).first().id

        if request.method == "POST":
            # Informacion inicial
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
            codigo_auto = generate_asset_code()
            return render(request, "home/enterAsset.html",{
                "code": codigo_auto,
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
            "AssetsValues": AssetsValue.objects.all()
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
                user = User.objects.create_user(
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
            return render(request, "tables/users.html",{
                "Workloads": Workload.objects.all(),
                "Departments": Departments.objects.all(),
                "message": "Ingrese el nombre del usuario"
            })
        
        if lastname == "" or lastname == None:
            return render(request, "tables/users.html",{
                "Workloads": Workload.objects.all(),
                "Departments": Departments.objects.all(),
                "message": "Ingrese el apellido del usuario"
            })
        
        if email == "" or email == None:
            return render(request, "tables/users.html",{
                "Workloads": Workload.objects.all(),
                "Departments": Departments.objects.all(),
                "message": "Ingrese el correo del usuario"
            })
        
        if celular == "" or celular == None:
            return render(request, "tables/users.html",{
                "Workloads": Workload.objects.all(),
                "Departments": Departments.objects.all(),
                "message": "Ingrese el celular del usuario"
            })
        
        if userDepartment == "" or userDepartment == None:
            return render(request, "tables/users.html",{
                "Workloads": Workload.objects.all(),
                "Departments": Departments.objects.all(),
                "message": "Seleccione el departamento del usuario"
            })
        
        if workload == "" or workload == None:
            return render(request, "tables/users.html",{
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
            return render(request, "tables/users.html",{
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
            return render(request, "tables/users.html",{
                "Workloads": Workload.objects.all(),
                "Departments": Departments.objects.all(),
                "message": f"Error al ingresar el usuario {e}"
            })
        
        return render(request, "tables/users.html",{
            "Users": User.objects.all(),
        })
    else:
        return render(request, "tables/users.html",{
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
    if request.user.is_authenticated:
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
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def asingRiskAsset(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            asset = request.POST.get("asset")
            risk = request.POST.get("risk")
            impact = request.POST.get("impact")
            probability = request.POST.get("probability")
            selected_risks = request.POST.getlist("selectedRisks")
            risks = []

            if asset == "" or asset == None:
                return render(request, "home/enterRisk.html",{
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": "Seleccione el activo"
                })
            
            if risk == "" or risk == None:
                return render(request, "home/enterRisk.html",{
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": "Seleccione el riesgo"
                })
            
            if selected_risks == "" or selected_risks == None:
                return render(request, "home/enterRisk.html",{
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": "Seleccione los riesgos"
                })
            
            if impact == "" or impact == None:
                return render(request, "home/enterRisk.html",{
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": "Seleccione el impacto"
                })
            
            if probability == "" or probability == None:
                return render(request, "home/enterRisk.html",{
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": "Seleccione la probabilidad"
                })
            
            asset = Assets.objects.get(pk=asset)
            risk = RiskType.objects.get(pk=risk)

            for selected_risk in selected_risks:
                risks.append(Risk.objects.get(pk=selected_risk))

            if (impact == "MA" and probability == "MA"):
                dimention = "MA"
            elif (impact == "A" and probability == "A"):
                dimention = "A"
            elif (impact == "M" and probability == "M"):
                dimention = "M"
            elif (impact == "B" and probability == "B"):
                dimention = "B"
            elif (impact == "MB" and probability == "MB"):
                dimention = "MB"
            elif (impact == "MA" and probability == "A"):
                dimention = "MA"
            elif (impact == "MA" and probability == "M"):
                dimention = "MA"
            elif (impact == "MA" and probability == "B"):
                dimention = "MA"
            elif (impact == "MA" and probability == "MB"):
                dimention = "A"
            elif (impact == "A" and probability == "MA"):
                dimention = "MA"
            elif (impact == "A" and probability == "M"):
                dimention = "A"
            elif (impact == "A" and probability == "B"):
                dimention = "A"
            elif (impact == "A" and probability == "MB"):
                dimention = "M"
            elif (impact == "M" and probability == "MA"):
                dimention = "A"
            elif (impact == "M" and probability == "A"):
                dimention = "A"
            elif (impact == "M" and probability == "B"):
                dimention = "M"
            elif (impact == "M" and probability == "MB"):  
                dimention = "B"
            elif (impact == "B" and probability == "MA"):
                dimention = "M"
            elif (impact == "B" and probability == "A"):
                dimention = "M"
            elif (impact == "B" and probability == "M"):
                dimention = "B"
            elif (impact == "B" and probability == "MB"):
                dimention = "MB"
            elif (impact == "MB" and probability == "MA"):
                dimention = "B"
            elif (impact == "MB" and probability == "A"):
                dimention = "B"
            elif (impact == "MB" and probability == "M"):
                dimention = "MB"
            elif (impact == "MB" and probability == "B"):
                dimention = "MB"
            else:
                return render(request, "home/enterRisk.html",{
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": "Seleccione el impacto y la probabilidad"
                })

            try:
                riskAsset = AssetsRisk(
                    asset=asset,
                    risktype=risk,
                    dimention=dimention
                )
                riskAsset.save()
                riskAsset.risk.set(risks)
            except Exception as e:
                return render(request, "home/enterRisk.html", {
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": f"Error al ingresar el riesgo {e}"
                })

            return render(request, "home/enterRisk.html", {
                "risktypes": RiskType.objects.all(),
                "assets": Assets.objects.all(),
            })
        else:
            return render(request, "home/enterRisk.html", {
                "risktypes": RiskType.objects.all(),
                "assets": Assets.objects.all(),
            })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def tableRisks(request):
    if request.user.is_authenticated:
        return render(request, "tables/risk.html",{
            "AssetsRisk": AssetsRisk.objects.all(),
        })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def deleteTableRisks(request, id):
    if request.user.is_authenticated:
        try:
            risk = AssetsRisk.objects.get(pk=id)
            risk.delete()
        except Exception as e:
            return render(request, "tables/risk.html",{
                "AssetsRisk": AssetsRisk.objects.all(),
                "message": f"Error al eliminar el riesgo {e}"
            })
        
        return render(request, "tables/risk.html",{
            "AssetsRisk": AssetsRisk.objects.all(),
        })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def editTableRisks(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            riskId = request.POST.get("riskId")
            asset = request.POST.get("asset")
            risk = request.POST.get("risk")
            impact = request.POST.get("impact")
            probability = request.POST.get("probability")
            selected_risks = request.POST.getlist("selectedRisks")
            risks = []

            if asset == "" or asset == None:
                return render(request, "home/enterRisk.html",{
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": "Seleccione el activo"
                })
            
            if risk == "" or risk == None:
                return render(request, "home/enterRisk.html",{
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": "Seleccione el riesgo"
                })
            
            if selected_risks == "" or selected_risks == None:
                return render(request, "home/enterRisk.html",{
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": "Seleccione los riesgos"
                })
            
            asset = Assets.objects.get(pk=asset)
            risk = RiskType.objects.get(pk=risk)

            for selected_risk in selected_risks:
                risks.append(Risk.objects.get(pk=selected_risk))

            if (impact == "MA" and probability == "MA"):
                dimention = "MA"
            elif (impact == "A" and probability == "A"):
                dimention = "A"
            elif (impact == "M" and probability == "M"):
                dimention = "M"
            elif (impact == "B" and probability == "B"):
                dimention = "B"
            elif (impact == "MB" and probability == "MB"):
                dimention = "MB"
            elif (impact == "MA" and probability == "A"):
                dimention = "MA"
            elif (impact == "MA" and probability == "M"):
                dimention = "MA"
            elif (impact == "MA" and probability == "B"):
                dimention = "MA"
            elif (impact == "MA" and probability == "MB"):
                dimention = "A"
            elif (impact == "A" and probability == "MA"):
                dimention = "MA"
            elif (impact == "A" and probability == "M"):
                dimention = "A"
            elif (impact == "A" and probability == "B"):
                dimention = "A"
            elif (impact == "A" and probability == "MB"):
                dimention = "M"
            elif (impact == "M" and probability == "MA"):
                dimention = "A"
            elif (impact == "M" and probability == "A"):
                dimention = "A"
            elif (impact == "M" and probability == "B"):
                dimention = "M"
            elif (impact == "M" and probability == "MB"):  
                dimention = "B"
            elif (impact == "B" and probability == "MA"):
                dimention = "M"
            elif (impact == "B" and probability == "A"):
                dimention = "M"
            elif (impact == "B" and probability == "M"):
                dimention = "B"
            elif (impact == "B" and probability == "MB"):
                dimention = "MB"
            elif (impact == "MB" and probability == "MA"):
                dimention = "B"
            elif (impact == "MB" and probability == "A"):
                dimention = "B"
            elif (impact == "MB" and probability == "M"):
                dimention = "MB"
            elif (impact == "MB" and probability == "B"):
                dimention = "MB"
            else:
                return render(request, "home/enterRisk.html",{
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": "Seleccione el impacto y la probabilidad"
                })

            try:
                AssetsRisk.objects.filter(pk=riskId).update(
                    asset=asset,
                    risktype=risk,
                    dimention=dimention
                )
                riskAsset = AssetsRisk.objects.get(pk=riskId)
                riskAsset.risk.set(risks)
            except Exception as e:
                return render(request, "home/enterRisk.html", {
                    "Assets": Assets.objects.all(),
                    "RiskTypes": RiskType.objects.all(),
                    "message": f"Error al ingresar el riesgo {e}"
                })

            return render(request, "tables/risk.html", {
                "AssetsRisk": AssetsRisk.objects.all(),
            })
        else:
            return render(request, "home/enterRisk.html", {
                "risktypes": RiskType.objects.all(),
                "assets": Assets.objects.all(),
            })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def enterSafeguards(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            assetrisk = request.POST.get("assetrisk")
            safeguard = request.POST.get("safeguard")
            addsafeguards = request.POST.getlist("selectedSafeguards")
            safeguards = []
            print(addsafeguards)

            if assetrisk == "" or assetrisk == None:
                return render(request, "home/enterSafeguards.html",{
                    "assetsRisk": AssetsRisk.objects.all(),
                    "Safeguards": Safeguards.objects.all(),
                    "message": "Seleccione el activo"
                })
            
            if safeguard == "" or safeguard == None:
                return render(request, "home/enterSafeguards.html",{
                    "assetsRisk": AssetsRisk.objects.all(),
                    "Safeguards": Safeguards.objects.all(),
                    "message": "Seleccione la salvaguarda"
                })
            
            if addsafeguards == "" or addsafeguards == None:
                return render(request, "home/enterSafeguards.html",{
                    "assetsRisk": AssetsRisk.objects.all(),
                    "Safeguards": Safeguards.objects.all(),
                    "message": "Seleccione las salvaguardas"
                })
            
            assetrisk = AssetsRisk.objects.get(pk=assetrisk)
            safeguard = Safeguards.objects.get(pk=safeguard)

            for addsafeguard in addsafeguards:
                safeguards.append(Safeguards.objects.get(pk=addsafeguard))

            print(safeguards)

            try:
                safeguardAssetRisk = SafeguardsRisk(
                    risk=assetrisk,
                )
                safeguardAssetRisk.save()
                safeguardAssetRisk.safeguard.set(safeguards)
            except Exception as e:
                return render(request, "home/enterSafeguards.html", {
                    "assetsRisk": AssetsRisk.objects.all(),
                    "Safeguards": Safeguards.objects.all(),
                    "message": f"Error al ingresar la salvaguarda {e}"
                })
            
            return render(request, "home/enterSafeguards.html", {
                "assetsRisk": AssetsRisk.objects.all(),
                "Safeguards": Safeguards.objects.all(),
            })
        else:
            return render(request, "home/enterSafeguards.html",{
                "assetsRisk": AssetsRisk.objects.all(),
            })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def tableSafeguards(request):
    if request.user.is_authenticated:
        return render(request, "tables/safeguards.html",{
            "Safeguards": SafeguardsRisk.objects.all(),
        })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def deleteTableSafeguards(request, id):
    if request.user.is_authenticated:
        try:
            safeguard = SafeguardsRisk.objects.get(pk=id)
            safeguard.delete()
        except Exception as e:
            return render(request, "tables/safeguards.html",{
                "Safeguards": SafeguardsRisk.objects.all(),
                "message": f"Error al eliminar la salvaguarda {e}"
            })
        
        return render(request, "tables/safeguards.html",{
            "Safeguards": SafeguardsRisk.objects.all(),
        })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))
    
def editTableSafeguards(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            safeguardId = request.POST.get("safeguardId")
            asset = request.POST.get("asset")
            selectedSafeguards = request.POST.getlist("selectedSafeguards")
            safeguards = []

            if asset == "" or asset == None:
                return render(request, "home/enterSafeguards.html",{
                    "assetsRisk": AssetsRisk.objects.all(),
                    "Safeguards": Safeguards.objects.all(),
                    "message": "Seleccione el activo"
                })
            
            if selectedSafeguards == "" or selectedSafeguards == None:
                return render(request, "home/enterSafeguards.html",{
                    "assetsRisk": AssetsRisk.objects.all(),
                    "Safeguards": Safeguards.objects.all(),
                    "message": "Seleccione las salvaguardas"
                })

            for selectedSafeguard in selectedSafeguards:
                safeguards.append(Safeguards.objects.get(pk=selectedSafeguard))

            try:
                safeguardAssetRisk = SafeguardsRisk.objects.get(pk=safeguardId)
                safeguardAssetRisk.safeguard.set(safeguards)
            except Exception as e:
                return render(request, "home/enterSafeguards.html", {
                    "assetsRisk": AssetsRisk.objects.all(),
                    "Safeguards": Safeguards.objects.all(),
                    "message": f"Error al ingresar la salvaguarda {e}"
                })
            
            return render(request, "tables/safeguards.html", {
                "Safeguards": SafeguardsRisk.objects.all(),
            })
    else:
        return HttpResponseRedirect(reverse("user:login_view"))

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

def get_risks(request, risktype_id):
    risk = Risk.objects.filter(type=risktype_id).values('id', 'name')
    return JsonResponse(list(risk), safe=False)

def get_risktypes(request):
    risktypes = RiskType.objects.all().values('id', 'name')
    return JsonResponse(list(risktypes), safe=False)

def get_safeguardstypes(request):
    safeguardstypes = SafeguardsTypes.objects.all().values('id', 'name')
    return JsonResponse(list(safeguardstypes), safe=False)

def get_safeguards(request, safeguardstype_id):
    safeguards = Safeguards.objects.filter(type=safeguardstype_id).values('id', 'code', 'name')
    return JsonResponse(list(safeguards), safe=False)