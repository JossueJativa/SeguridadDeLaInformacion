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
                    ubicationTipe = ubicationType,
                    ubication = ubication,
                    quantity = quantity,
                    characteristic = characteristic,
                    tipe = type,
                    responsableArea = responsableArea,
                    responsableUser = responsablePerson
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
                        # Activacion del toggle 2
                        "state2": state2,
                        "valorationDimention": valorationDimention,
                        "valorationAssing": valorationAssing,
                        "cualitative": cualitative,
                        "descriptionValue": descriptionValue,
                        "message": "Seleccione de que depende"
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
                        # Activacion del toggle 1
                        "state": state,
                        "dependency": dependency,
                        "descriptionDependency": descriptionDependency,
                        "responsableUser": responsableUser,
                        "dependsOf": dependsOf,
                        # Activacion del toggle 2
                        "state2": state2,
                        "valorationAssing": valorationAssing,
                        "cualitative": cualitative,
                        "descriptionValue": descriptionValue,
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
                        # Activacion del toggle 1
                        "state": state,
                        "dependency": dependency,
                        "descriptionDependency": descriptionDependency,
                        "responsableUser": responsableUser,
                        "dependsOf": dependsOf,
                        # Activacion del toggle 2
                        "state2": state2,
                        "valorationDimention": valorationDimention,
                        "cualitative": cualitative,
                        "descriptionValue": descriptionValue,
                        "message": "Seleccione la valoración"
                    })
                
            # Logica para guardar el asset
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
                    username=username
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
            "Users": User.objects.all()
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
    
def get_subtypes(request, type_id):
    subtypes = SubtypeAssets.objects.filter(type_id=type_id).values('id', 'name')
    return JsonResponse(list(subtypes), safe=False)