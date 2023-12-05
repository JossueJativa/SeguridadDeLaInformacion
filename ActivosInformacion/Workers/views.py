from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from Users.models import Responsabilities, User, Department, UserResponsabilities, WorkPosition
from CompanyAssets.models import CompanyAssets

# Create your views here.
def userspage(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            identity = request.POST.get("identity")
            username = request.POST.get("username")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            department = request.POST.get("department")
            workposition = request.POST.get("workPosition")
            password = request.POST.get("password")
            confirm_password = request.POST.get("password2")

            if password != confirm_password:
                users = User.objects.all()
                departments = Department.objects.all()
                workpositions = WorkPosition.objects.all()
                error_message = "Las contraseñas no coinciden"
                return render(request, "users.html",{
                    "users": users,
                    "departments": departments,
                    "workpositions": workpositions,
                    "error_message": error_message,
                })

            try:
                if User.objects.get(identity=identity):
                    users = User.objects.all()
                    departments = Department.objects.all()
                    workpositions = WorkPosition.objects.all()
                    error_message = f"El usuario ya existe cedula: {identity}"
                    return render(request, "users.html",{
                        "users": users,
                        "departments": departments,
                        "workpositions": workpositions,
                        "error_message": error_message,
                    })
            except:
                pass

            try:
                if User.objects.get(email=email):
                    users = User.objects.all()
                    departments = Department.objects.all()
                    workpositions = WorkPosition.objects.all()
                    error_message = f"El usuario ya existe email: {email}"
                    return render(request, "users.html",{
                        "users": users,
                        "departments": departments,
                        "workpositions": workpositions,
                        "error_message": error_message,
                    })
            except:
                pass

            department = Department.objects.get(pk=department)
            workposition = WorkPosition.objects.get(pk=workposition)

            user = User.objects.create_user(
                username=username, 
                email=email, 
                password=password,
                department=department,
                workPosition = workposition
            )
            user.first_name = first_name
            user.last_name = last_name
            user.identity = identity
            user.save()

            users = User.objects.all()
            departments = Department.objects.all()
            workpositions = WorkPosition.objects.all()
            return render(request, "users.html",{
                "users": users,
                "departments": departments,
                "workpositions": workpositions,
            })
        else:
            users = User.objects.all()
            departments = Department.objects.all()
            workpositions = WorkPosition.objects.all()
            return render(request, "users.html",{
                "users": users,
                "departments": departments,
                "workpositions": workpositions,
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def deleteuser(request, user_id):
    if request.user.is_authenticated:
        user = User.objects.get(pk=user_id)
        user.delete()
        users = User.objects.all()
        departments = Department.objects.all()
        workpositions = WorkPosition.objects.all()
        return render(request, "users.html",{
            "users": users,
            "departments": departments,
            "workpositions": workpositions,
        })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def edituser(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user_id = request.POST.get("id")
            identity = request.POST.get("identity")
            username = request.POST.get("username")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            department = request.POST.get("department")
            workposition = request.POST.get("workPosition")
            password = request.POST.get("password")
            confirm_password = request.POST.get("password2")

            if password != confirm_password:
                users = User.objects.all()
                departments = Department.objects.all()
                workpositions = WorkPosition.objects.all()
                error_message = "Las contraseñas no coinciden"
                return render(request, "users.html",{
                    "users": users,
                    "departments": departments,
                    "workpositions": workpositions,
                    "error_message": error_message,
                })

            department = Department.objects.get(pk=department)
            workposition = WorkPosition.objects.get(pk=workposition)

            user = User.objects.get(pk=user_id)
            user.username = username
            user.email = email
            user.password = password
            user.department = department
            user.workPosition = workposition
            user.first_name = first_name
            user.last_name = last_name
            user.identity = identity
            user.save()

            users = User.objects.all()
            departments = Department.objects.all()
            workpositions = WorkPosition.objects.all()
            return render(request, "users.html",{
                "users": users,
                "departments": departments,
                "workpositions": workpositions,
            })
        else:
            users = User.objects.all()
            departments = Department.objects.all()
            workpositions = WorkPosition.objects.all()
            return render(request, "users.html",{
                "users": users,
                "departments": departments,
                "workpositions": workpositions,
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def departments(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get("name")
            department = Department.objects.create(name=name)
            departments = Department.objects.all()
            return render(request, "departments.html",{
                "departments": departments,
            })
        else:
            departments = Department.objects.all()
            return render(request, "departments.html",{
                "departments": departments,
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def deletedepartment(request, department_id):
    if request.user.is_authenticated:
        department = Department.objects.get(pk=department_id)
        department.delete()
        departments = Department.objects.all()
        return render(request, "departments.html",{
            "departments": departments,
        })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def editdepartment(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            department_id = request.POST.get("id")
            name = request.POST.get("name")
            department = Department.objects.get(pk=department_id)
            department.name = name
            department.save()
            departments = Department.objects.all()
            return render(request, "departments.html",{
                "departments": departments,
            })
        else:
            departments = Department.objects.all()
            return render(request, "departments.html",{
                "departments": departments,
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def workpositions(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get("name")
            workposition = WorkPosition.objects.create(name=name)
            workpositions = WorkPosition.objects.all()
            return render(request, "workpositions.html",{
                "workpositions": workpositions,
            })
        else:
            workpositions = WorkPosition.objects.all()
            return render(request, "workpositions.html",{
                "workpositions": workpositions,
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def deleteworkposition(request, workposition_id):
    if request.user.is_authenticated:
        workposition = WorkPosition.objects.get(pk=workposition_id)
        workposition.delete()
        workpositions = WorkPosition.objects.all()
        return render(request, "workpositions.html",{
            "workpositions": workpositions,
        })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def editworkposition(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            workposition_id = request.POST.get("id")
            name = request.POST.get("name")
            workposition = WorkPosition.objects.get(pk=workposition_id)
            workposition.name = name
            workposition.save()
            workpositions = WorkPosition.objects.all()
            return render(request, "workpositions.html",{
                "workpositions": workpositions,
            })
        else:
            workpositions = WorkPosition.objects.all()
            return render(request, "workpositions.html",{
                "workpositions": workpositions,
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def responsabilities(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get("name")
            responsability = Responsabilities.objects.create(name=name)
            responsabilities = Responsabilities.objects.all()
            return render(request, "responsabilities.html",{
                "responsabilities": responsabilities,
            })
        else:
            responsabilities = Responsabilities.objects.all()
            return render(request, "responsabilities.html",{
                "responsabilities": responsabilities,
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def deleteresponsability(request, responsability_id):
    if request.user.is_authenticated:
        responsability = Responsabilities.objects.get(pk=responsability_id)
        responsability.delete()
        responsabilities = Responsabilities.objects.all()
        return render(request, "responsabilities.html",{
            "responsabilities": responsabilities,
        })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def editresponsability(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            responsability_id = request.POST.get("id")
            name = request.POST.get("name")
            responsability = Responsabilities.objects.get(pk=responsability_id)
            responsability.name = name
            responsability.save()
            responsabilities = Responsabilities.objects.all()
            return render(request, "responsabilities.html",{
                "responsabilities": responsabilities,
            })
        else:
            responsabilities = Responsabilities.objects.all()
            return render(request, "responsabilities.html",{
                "responsabilities": responsabilities,
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def userresponsabilities(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user_id = request.POST.get("user")
            responsability_id = request.POST.get("responsability")
            user = User.objects.get(pk=user_id)
            responsability = Responsabilities.objects.get(pk=responsability_id)
            userresponsability = UserResponsabilities.objects.create(
                user=user,
                responsability=responsability,
            )
            userresponsability.save()
            users = User.objects.all()
            responsabilities = Responsabilities.objects.all()
            uresponsabilities = UserResponsabilities.objects.all()
            return render(request, "userresponsabilities.html",{
                "users": users,
                "responsabilities": responsabilities,
                "uresponsabilities": uresponsabilities,
            })
        else:
            users = User.objects.all()
            responsabilities = Responsabilities.objects.all()
            uresponsabilities = UserResponsabilities.objects.all()
            return render(request, "userresponsabilities.html",{
                "users": users,
                "responsabilities": responsabilities,
                "uresponsabilities": uresponsabilities,
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def deleteuserresponsability(request, userresponsability_id):
    if request.user.is_authenticated:
        userresponsability = UserResponsabilities.objects.get(pk=userresponsability_id)
        userresponsability.delete()
        users = User.objects.all()
        responsabilities = Responsabilities.objects.all()
        uresponsabilities = UserResponsabilities.objects.all()
        return render(request, "userresponsabilities.html",{
            "users": users,
            "responsabilities": responsabilities,
            "uresponsabilities": uresponsabilities,
        })
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def edituserresponsability(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            userresponsability_id = request.POST.get("id")
            user_id = request.POST.get("user")
            responsability_id = request.POST.get("responsability")
            user = User.objects.get(pk=user_id)
            responsability = Responsabilities.objects.get(pk=responsability_id)
            userresponsability = UserResponsabilities.objects.get(pk=userresponsability_id)
            userresponsability.user = user
            userresponsability.responsability = responsability
            userresponsability.save()
            users = User.objects.all()
            responsabilities = Responsabilities.objects.all()
            uresponsabilities = UserResponsabilities.objects.all()
            return render(request, "userresponsabilities.html",{
                "users": users,
                "responsabilities": responsabilities,
                "uresponsabilities": uresponsabilities,
            })
        else:
            users = User.objects.all()
            responsabilities = Responsabilities.objects.all()
            uresponsabilities = UserResponsabilities.objects.all()
            return render(request, "userresponsabilities.html",{
                "users": users,
                "responsabilities": responsabilities,
                "uresponsabilities": uresponsabilities,
            })
    else:
        return HttpResponseRedirect(reverse("user:login"))