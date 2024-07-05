from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html") 

def rando(request):
    return HttpResponse("Hello Rando!") 

def greet(request, name: str):
    # third param is a dictionary of values
    return render(request, "Hello/greet.html", {
        "name": name.capitalize()
    })

