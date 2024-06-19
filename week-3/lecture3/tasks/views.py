from django import forms
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# this is a "global" var for ALL users, changed to a session
# tasks = []

# create a form with one field with the name "task"
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)
    

# Create your views here.
def index(request: HttpRequest):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request: HttpRequest):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():   #server side validation
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
            
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })