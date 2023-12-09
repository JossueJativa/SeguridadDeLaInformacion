from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

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

def logout_view(request):
    logout(request)
    return render(request, "login/login.html")