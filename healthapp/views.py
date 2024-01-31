
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from.models import*
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('dashboard')
        
    return render(request, "login.html")

def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(firstname, email, password)
        user = authenticate(request, username=firstname, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        
    return render(request, "signup.html")
