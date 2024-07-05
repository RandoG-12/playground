from django.urls import path
from . import views

urlpatterns = [
    # /newyear
    path("", views.index, name="index")
]