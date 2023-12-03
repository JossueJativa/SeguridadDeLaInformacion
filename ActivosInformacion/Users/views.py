from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login as django_login, logout
from django.urls import reverse

from Users.models import User, TeamRoles

# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")


        error_message = "Username or password are incorrect"
        

        try:
            username = User.objects.get(email=email).username
            user = authenticate(username=username, password=password)
            if user:
                django_login(request, user)
                return HttpResponseRedirect(reverse("home:home"))
            else:
                return render(request, "login/login.html", {
                    "error_message": error_message,
                    "email": email,
                })
        except Exception as e:
            print(e)
            error_message = "Something went wrong"
            return render(request, "login/login.html", {
                "error_message": error_message,
                "email": email,
            })
    return render(request, "login/login.html")

def register(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        identity = request.POST.get("identity")
        jobtype = request.POST.get("jobtype")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")

        try:
            user = User.objects.get(email=email)
        except:
            user = None

        try:
            user = User.objects.get(identity=identity)
        except:
            user = None

        if user:
            error_message = "Email already taken"
            return render(request, "login/register.html", {
                "error_message": error_message,
                "error_message": error_message,
                "firstname": firstname,
                "lastname": lastname,
                "username": username,
                "identity": identity,
                "jobtype": jobtype,
            })

        if password != confirm:
            error_message = "Passwords do not match"
            return render(request, "login/register.html", {
                "error_message": error_message,
                "error_message": error_message,
                "firstname": firstname,
                "lastname": lastname,
                "username": username,
                "email": email,
                "identity": identity,
                "jobtype": jobtype,
            })
        
        teamRole = TeamRoles.objects.create(
            name=jobtype
        )
        teamRole.save()

        user = User.objects.create_user(
            username=username, 
            email=email, 
            password=password
        )
        user.first_name = firstname
        user.last_name = lastname
        user.identity = identity
        user.teamRole = teamRole
        user.save()

        return render(request, "login/login.html")
    return render(request, "login/register.html")

def recover(request):
    return render(request, "login/recover.html")

def logout_view(request):
    logout(request)
    return render(request, "login/login.html")