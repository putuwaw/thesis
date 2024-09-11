from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest


@login_required
def dashboard_home(request: WSGIRequest):
    # Get the current logged-in user's name
    username = request.user.username

    # get query parameter
    origin = request.GET.get("origin")

    ctx = {
        "username": username,
        "origin": origin,
    }
    return render(request, "dashboard/home.html", ctx)


@login_required
def dashboard_data(request: WSGIRequest):
    return render(request, "dashboard/data.html")


@login_required
def dashboard_training(request: WSGIRequest):
    return render(request, "dashboard/training.html")


@login_required
def dashboard_testing(request: WSGIRequest):
    return render(request, "dashboard/testing.html")
