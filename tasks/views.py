from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_world(request):
    context = {}
    return render(request, template_name='signup.html', context=context)