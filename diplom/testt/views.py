from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

menu = ["1","2","3"]

def index(request):
    posts = Women.objects.all()
    return render(request, 'testt/index.html', {'posts' : posts ,'menu': menu, 'title': 'Главная'})

def about(request):
    return render(request, 'testt/about.html', {'menu': menu, 'title': 'О сайте'})

def categories(request, csid):
    return HttpResponse(f"<h1>СТраница приложения testt<h1><p>{csid}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена<h1>")
