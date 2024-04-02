from django.shortcuts import HttpResponse, render


# Create your views here.
def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome}! Tais com {idade} anos já hein!</h1>')