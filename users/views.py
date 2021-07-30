from django.shortcuts import redirect, render
from django.contrib import auth


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("snsapp:home")
        else:
            return render(request, "users/bad_login.html")
    else:
        return render(request, "users/login.html")


def logout(request):
    auth.logout(request)
    return redirect("snsapp:home")
