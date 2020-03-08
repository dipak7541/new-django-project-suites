from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('/about', views.about, name = "about"),
    path('/contact', views.contact, name ="contact"),
    path('/events', views.events, name = "events"),
    path('/rooms', views.rooms, name = "rooms"),
    path('/form', views.getform, name="getfrom"),
    
]