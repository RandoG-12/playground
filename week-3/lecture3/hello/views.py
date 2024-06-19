from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html") 

def rando(request):
    return HttpResponse("Hello Rando!") 

def greet(request, name):
    return HttpResponse(f"Hello {name.capitalize()}.") 

