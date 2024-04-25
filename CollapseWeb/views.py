from django.shortcuts import render, HttpResponse
from .models import Client

def index(request: HttpResponse):
    return render(request, 'index.html', {'clients': Client.objects.all()})

def api(request: HttpResponse):
    return render(request, 'api.html')