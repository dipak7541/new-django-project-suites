from django.shortcuts import render, redirect
from .models import ManxekoBichar

def index(request):
   
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def events(request):
    return render(request, 'events.html')

def rooms(request):
    return render(request, 'rooms.html')
    
def contact(request):
    return render(request, 'contact.html')
# Create your views here.

def getform(request):
    name = request.POST['name']
    comments=request.POST['comments']
    date=request.POST['datepicker']

    form1= ManxekoBichar(name=name,comments=comments,date=date)
    form1.save()
    print("sucess")
    return redirect('/suite')