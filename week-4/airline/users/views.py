from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def index(request: HttpRequest):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:view-login'))
    else:
        return render(request, 'users/index.html')

def login_view(request: HttpRequest):
    #bob/bobsmith      mary/marysmith
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('users:view-index'))
        else:
            return render(request, 'users/login.html', {
                'message': 'Invalid credentials'
            })
    else:
        return render(request, 'users/login.html')

def logout_view(request: HttpRequest):
    logout(request)
    return render(request, 'users/login.html', {
        'message': 'Logged out.'
    })
