from django.shortcuts import render
from .models import PeopleSay

def index(request):
    people1= PeopleSay.objects.all()
    return render(request, 'index.html', {'people': people1})

def about(request):
    return render(request, 'about.html')

def events(request):
    return render(request, 'events.html')

def rooms(request):
    return render(request, 'rooms.html')
    
def contact(request):
    return render(request, 'contact.html')
# Create your views here.
