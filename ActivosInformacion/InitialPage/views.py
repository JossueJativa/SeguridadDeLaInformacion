from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from InitialPage.models import Departments
from Users.models import User, Workload

# Create your views here.
def enterAsset(request):
    if request.user.is_authenticated:
        return render(request, "home/enterAsset.html")
    else:
        return HttpResponseRedirect(reverse("user:login_view"))

def enterUsers(request):
    if request.user.is_authenticated:
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
                    "Departments": Departments.objects.all(),
                    "message": "Ingrese el nombre del usuario"
                })
            
            if lastname == "" or lastname == None:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": Departments.objects.all(),
                    "message": "Ingrese el apellido del usuario"
                })
            
            if email == "" or email == None:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": Departments.objects.all(),
                    "message": "Ingrese el correo del usuario"
                })
            
            if celular == "" or celular == None:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": Departments.objects.all(),
                    "message": "Ingrese la identidad del usuario"
                })
            
            if password == "" or password == None:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": Departments.objects.all(),
                    "message": "Ingrese la contraseña del usuario"
                })
            
            if confirm == "" or confirm == None:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": Departments.objects.all(),
                    "message": "Confirme la contraseña del usuario"
                })
            
            if userDepartment == "" or userDepartment == None:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": Departments.objects.all(),
                    "message": "Seleccione el departamento del usuario"
                })
            
            if workload == "" or workload == None:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": Departments.objects.all(),
                    "message": "Seleccione la carga de trabajo del usuario"
                })
            
            if password != confirm:
                return render(request, "home/enterUsers.html",{
                    "Workloads": Workload.objects.all(),
                    "Departments": Departments.objects.all(),
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
                    "Departments": Departments.objects.all(),
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
                    "Departments": Departments.objects.all(),
                    "message": f"Error al ingresar el usuario {e}"
                })
            
            return render(request, "tables/users.html",{
                "Users": User.objects.all(),
            })
        return render(request, "home/enterUsers.html",{
            "Workloads": Workload.objects.all(),
            "Departments": Departments.objects.all()
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