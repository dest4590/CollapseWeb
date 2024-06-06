from django.shortcuts import render, HttpResponse

def index(request: HttpResponse):
    return render(request, 'api.html')