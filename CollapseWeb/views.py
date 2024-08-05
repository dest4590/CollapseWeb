from django.shortcuts import render, HttpResponse
from .models import ClientLoader, Config

def index(request: HttpResponse):
    return render(request, 'index.html', {
        'clients': ClientLoader.objects.all(),
        'configs': Config.objects.all()
        })

def api(request: HttpResponse):
    return render(request, 'api.html')

def custom_404(request, exception):
    return render(request, '418.html', status=418)