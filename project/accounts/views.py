from django.shortcuts import render, HttpResponse

# Create 
#  views here.

def Register(request):
    return render(request, 'register.html')

def Login(request):
    return render(request, 'login.html')