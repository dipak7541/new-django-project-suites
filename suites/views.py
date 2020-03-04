from django.shortcuts import render

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
