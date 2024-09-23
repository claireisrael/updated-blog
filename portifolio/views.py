from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from portifolio import models
from portifolio.models import Contact

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def contact(request):
    if request.method == 'POST':
        print('post')
        name = request.POST['Name']
        email = request.POST['Email']
        Number = request.POST['Number']
        Message = request.POST['Message']
        print(name, email,Number ,Message)

        if len(name) > 1 and len(name) < 30:
            pass
        else:
            messages.error(request, 'Name must be between 2 and 30 characters')
            return redirect(request,'blog/home.html')
            
        if len(email) >1 and len(email) < 30:
            pass
        else:
            messages.error(request, 'Email must be between 2 and 30 characters')
            return redirect(request,'blog/home.html')
        print(len(Number))
        if len(Number) > 9 and len(Number) < 10:
            pass
        else:
            messages.error(request, 'Number must be 10 digits')
            return redirect(request,'blog/home.html')
        ins = models.Contact(name = name,email = email, Number = Number,Message = Message)
        ins.save()
        messages.success(request, 'Thanks for contacting me your message has been sent successfully.')
        print('data sent to the database')

        print('The request is no pass')
    return render(request, 'blog/contact.html')
        
