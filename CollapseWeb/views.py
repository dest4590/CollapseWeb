from django.shortcuts import render, HttpResponse
from .models import Client

def index(request: HttpResponse):
    return render(request, 'index.html', {'clients': Client.objects.filter(hidden=False)})

def api(request: HttpResponse):
    return render(request, 'api.html')