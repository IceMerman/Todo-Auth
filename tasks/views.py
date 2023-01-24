from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ValidationError
from .forms import createTaskForm
from .models import Task

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
    # tasks = Task.objects.filter(user=request.user, date_completed__isnull=True)
    tasks = Task.objects.filter(user=request.user)
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/tasks.html', context=context)

def task_detail(request, id_task: int):
    task = get_object_or_404(Task, pk=id_task)
    # task = Task.objects.get(pk=id_task)
    context = {
        'task': task
    }
    return render(request, 'tasks/detail.html', context=context)


def create_task(request):
    context = {}
    if request.method=="GET":
        context['form'] = createTaskForm
    elif request.method=="POST":
        try:
            form = createTaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()     
            return redirect('tasks')
        except Exception as e:
            context['message'] = f'Hubo un error, intenta de nuevo: {e}'
            context['form'] = createTaskForm

    return render(request, 'tasks/create_task.html', context=context)


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