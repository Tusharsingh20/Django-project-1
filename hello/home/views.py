from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from .models import Contact

# Create your views here.

# def index(request):
# return HttpResponse("this is a home page")


def index(request):
    context = {
        "variable": 'this is var 1',
        "variable2": 'this is var 2'
    }
    messages.success(request,"Welcome Anime lovers")
    return render(request, 'index.html', context)


def about(request):
    # return HttpResponse("this is a about page")
    return render(request, 'about.html')

def services(request):
    # return HttpResponse("this is a services page")
    return render(request, 'services.html')


def contact(request):
    # return HttpResponse("this is a contact page")
    # messages.error(request,"Welcome to contact")
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        feedback = request.POST.get('feedback')

        if len(name)<20 or len(email)<6 or len(phone)<10 or len(feedback):
            messages.error(request,"!! Please Fill the Correctly Details")
        else:
            contact=Contact(name=name, email=email, phone=phone, feedback=feedback,date=datetime.today())
            contact.save()
            messages.success(request,"Contact is submitted successfully")
    return render(request, 'contact.html')  