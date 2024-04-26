from django.shortcuts import render, HttpResponse
from .models import Client

def is_admin(user):
    return user.is_superuser

def index(request: HttpResponse):
    return render(request, 'index.html', {'clients': Client.objects.all(), 'is_admin': True if request.user.is_superuser else False})

def api(request: HttpResponse):
    return render(request, 'api.html')