from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ValidationError
from .forms import createTaskForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required

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


@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, date_completed__isnull=True)
    # tasks = Task.objects.filter(user=request.user)
    context = {
        'tasks': tasks,
        'completed': False
    }
    return render(request, 'tasks/tasks.html', context=context)


@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(
        user=request.user, date_completed__isnull=False).order_by('-date_completed')
    # tasks = Task.objects.filter(user=request.user)
    context = {
        'tasks': tasks,
        'completed': True
    }
    return render(request, 'tasks/tasks.html', context=context)


@login_required
def task_detail(request, id_task: int):
    context = {}
    task = get_object_or_404(Task, pk=id_task, user=request.user)
    if request.method == "GET":
        context['form'] = createTaskForm(instance=task)
        context['task'] = task
        return render(request, 'tasks/detail.html', context=context)
    elif request.method == "POST":
        try:
            form = createTaskForm(request.POST, instance=task)
            context['form'] = form
            context['task'] = task
            form.save()
        except ValueError:
            context['message'] = "ValueError"
            return render(request, 'tasks/detail.html', context=context)
        # return redirect('task_detail', id_task=id_task)
        return redirect('tasks')


@login_required
def task_complete(request, id_task: int):
    # context = {}
    task = get_object_or_404(Task, pk=id_task, user=request.user)
    if request.method == "POST":
        task.date_completed = timezone.now()
        task.save()
    return redirect('tasks')


@login_required
def task_delete(request, id_task: int):
    # context = {}
    task = get_object_or_404(Task, pk=id_task, user=request.user)
    if request.method == "POST":
        task.delete()
    return redirect('tasks')


@login_required
def create_task(request):
    context = {}
    if request.method == "GET":
        context['form'] = createTaskForm
    elif request.method == "POST":
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


@login_required
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
            context = {
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
