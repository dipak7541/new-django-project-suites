from django.shortcuts import render, redirect
from .models import ManxekoBichar, ContactDetails

def index(request):
    peoples =ManxekoBichar.objects.all()
    return render(request, 'index.html',{'peoples':peoples})

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

def contactform(request):
    fullname = request.POST.get('fullname')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    message = request.POST.get('message')
    #date = request.POST.get('date')

    form2 = ContactDetails(name=fullname,email=email,phoneno=phone,message=message)
    form2.save()
    print('sucess')
    return redirect('/suite/contact')
