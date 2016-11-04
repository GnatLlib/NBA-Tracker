from django.shortcuts import render, redirect
from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,

    )
from .forms import UserLoginForm


def index(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username, password=password)
        login(request,user)
        return redirect("/profile")

    return render(request, "home/index.html", {"form":form})
