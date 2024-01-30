
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from.models import*
from django.contrib.auth.models import User

def index(request):
    return render(request, "index.html")

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('home')
        
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
            return redirect('index')
        
    return render(request, "signup.html")