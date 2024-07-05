from django.urls import path

from . import views

app_name = "flights"

urlpatterns = [
    path('', views.index, name='view-index'),
    path('<int:flight_id>', views.get_flight, name='view-get-flight')
]

