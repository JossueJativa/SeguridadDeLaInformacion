from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            userlogin = authenticate(request, username=username, password=password)
        except:
            userlogin = None

        if userlogin is not None:
            login(request, userlogin)
            return render(request, "home/enterAsset.html")
        else:
            return render(request, "login/login.html", {
                "message": "Usuario o contraseña incorrectos"
            })

    return render(request, "login/login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm = request.POST.get("password2")
        email = request.POST.get("email")

        if password == confirm:
            try:
                user = User.objects.create_user(username, password=password, email=email)
                user.save()
                return render(request, "login/login.html", {
                    "message": "Usuario creado correctamente"
                })
            except:
                return render(request, "register/register.html", {
                    "message": "El usuario ya existe"
                })
        else:
            return render(request, "register/register.html", {
                "message": "Las contraseñas no coinciden"
            })
        
    return render(request, "register/register.html")

def logout_view(request):
    logout(request)
    return render(request, "login/login.html")