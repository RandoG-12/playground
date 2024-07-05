from django.shortcuts import render
from datetime import date

def index(request):
    newyear = date.today().month == 1 and date.today().day == 1 
    return render(request, "newyear/index.html", {
        "newyear": newyear
    })
