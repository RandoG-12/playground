from django.urls import path
from . import views

urlpatterns = [
    # /hello
    path("", views.index, name="index"),
    
    # /hello/rando
    path("rando", views.rando, name="rando"),

    # /hello/bastage
    path("bastage", views.rando, name="rando"),

    # /hello/a/b/c
    path("a/b/c", views.rando, name="rando"),

    # /hello/a/b/c
    path("<str:name>", views.greet, name="greet")
]