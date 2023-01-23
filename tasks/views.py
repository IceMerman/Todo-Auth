from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ValidationError

# Create your views here.


def home(request):
    context = {}
    return render(request, template_name='home.html', context=context)


def signup(request):
    # #Juasd1238asd!"#ads"
    context = {}
    if request.method == "POST":
        newUser = UserCreationForm(data=request.POST)
        if newUser.is_valid():
            user = newUser.save()
            # user = User.objects.get(username=request.POST['username'])
            login(request, user)
            return redirect('tasks')
        else:
            context.update(newUser.error_messages)
        return render(request, template_name='signup.html', context=context)

    elif request.method == "GET":
        context = {
            'form': UserCreationForm
        }
    return render(request, template_name='signup.html', context=context)


def tasks(request):
    context = {}
    return render(request, 'tasks.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'POST':
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('tasks')
        else:
            context={
                'form': AuthenticationForm,
                'error': "Invalid credentials"
            }
        # user = AuthenticationForm(request)
        # try:
        #     user.confirm_login_allowed()
        #     login(request, user.get_user())
        # except ValidationError:
        #     return
    else:
        context = {'form': AuthenticationForm}
    return render(request, 'signin.html', context=context)
