from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    if(request.GET):
        print(request.GET)
    return HttpResponse("СТраница приложения testt")

def categories(request, csid):
    return HttpResponse(f"<h1>СТраница приложения testt<h1><p>{csid}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена<h1>")
