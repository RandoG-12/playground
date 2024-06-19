# from django.http import HttpResponse
from django.shortcuts import render

# "global" vars to the app?
tasks = ["foo", "bar", "baz"]

# Create your views here.
def index(request): 
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    return render(request, "tasks/add.html")