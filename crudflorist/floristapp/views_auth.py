from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


# Vista de bienvenida
def home_view(request):
    return render(request, "auth/home.html")  # plantillas en floristapp/templates/auth/


# Login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.is_superuser:
                return redirect("dashboard_admin")
            else:
                return redirect("producto_list")
    else:
        form = AuthenticationForm()
    return render(request, "auth/login.html", {"form": form})


# Registro
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "auth/register.html", {"form": form})


# Logout
@login_required
def logout_view(request):
    logout(request)
    return redirect("home")
