from django.shortcuts import render, HttpResponse

# Create 
#  views here.

def test(request):
    return render(request, 'register.html')