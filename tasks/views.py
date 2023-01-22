from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db import IntegrityError

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

            # if request.POST['password1'] == request.POST['password2']:
            #     try:
            #         user = User.objects.create_user(username=request.POST['username'], password=request.POST['password2'])
            #         user.save()
            #     except IntegrityError:
            #         context['error'] = 'Error user already exists'

            #     except Exception as e:
            #         return HttpResponse(f'Error {e}')
            # else:
                # context['error'] = 'No coinciden las constraseñas'
        return render(request, template_name='signup.html', context=context)
        
    elif request.method=="GET":
        context = {
            'form': UserCreationForm
        }
    return render(request, template_name='signup.html', context=context)