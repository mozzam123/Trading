from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import *


def Register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")  # Retrieve email from the form
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {"username_error": "Username already exists"})
        # Create a new User object and save it to the database
        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()
        print("user savved")

    return render(request, 'register.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get('loginpassword')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print('Logged in')
            return redirect('home')
        else:
            # Authentication failed
            print("Not loggedin")
            error_message = "Invalid username or password"
            return render(request, 'login.html', {"error_message": error_message})

    return render(request, 'login.html')


def home(request):
    strategies = Strategy.objects.all()
    fields = Strategy._meta.get_fields()
    return render(request, 'home.html', {'strategies': strategies, "fields": fields})
