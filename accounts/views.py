import requests
from django.shortcuts import render, redirect
from BoxScore.linescraper import getgames
from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,

    )
from .forms import UserLoginForm, UserRegisterForm
from BoxScore.models import QuarterScore


def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        login(request, user)
        return redirect("/profile")
    return render(request, "register.html", {"form":form})


def logout_view(request):
    logout(request)
    return redirect("/")


def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('/')

    # request stats.nba
    games = getgames()
    
    scorelines = []
    # pull basic scoreline data from game objects
    for game in games:
        s1 = str(game.t1_overview["team"]) + " " + str(game.t1_overview["q1"]) + " " + str(game.t1_overview["q2"]) + \
             " " + str(game.t1_overview["q3"]) + " " + str(game.t1_overview["q4"]) + " " + str(game.t1_overview["total"])
        s2 = str(game.t2_overview["team"]) + " " + str(game.t2_overview["q1"]) + " " + str(game.t2_overview["q2"]) + \
            " " + str(game.t2_overview["q3"]) + " " + str(game.t2_overview["q4"]) + " " + str(game.t2_overview["total"])
        scorelines.append([s1, s2])
    return render(request, "profile.html", {"scorelines": scorelines})

