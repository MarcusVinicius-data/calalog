from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'new_catalog/home.html')


def contato(request):
    return HttpResponse('contato')


def sobre(request):
    return HttpResponse('sobre')