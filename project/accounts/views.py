from django.shortcuts import render, HttpResponse

# Create 
#  views here.

def Register(request):
    return render(request, 'register.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get('loginpassword')

        print(username, password)
    return render(request, 'login.html')