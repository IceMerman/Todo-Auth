from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {}
    return render(request, template_name='home.html', context=context)

def signup(request):
    
    context = {}
    if request.method=="POST":
        newUser = UserCreationForm(data=request.POST)
        if newUser.is_valid():
            newUser.save()
            return redirect('home')
        else:
            context.update(newUser.error_messages)
        return render(request, template_name='signup.html', context=context)
        
    elif request.method=="GET":
        context = {
            'form': UserCreationForm
        }
    return render(request, template_name='signup.html', context=context)