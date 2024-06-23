from django.shortcuts import render, HttpResponse

def index(request: HttpResponse):
    return render(request, 'api.html')

def custom_404(request, exception):
    return render(request, '418.html', status=418)