from django.urls import path
from . import views

urlpatterns = [
    # /tasks
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]