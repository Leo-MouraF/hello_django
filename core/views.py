from django.shortcuts import HttpResponse, render


# Create your views here.
def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome}! Tais com {idade} anos já hein!</h1>')

def soma(request, n1, n2):
    return HttpResponse(f'{n1} + {n2} = {n1+n2}')

def subtracao(request, n1, n2):
    return HttpResponse(f'{n1} - {n2} = {n1-n2}')

def multiplicacao(request, n1, n2):
    return HttpResponse(f'{n1} * {n2} = {n1*n2}')

def divisao(request, n1, n2):
    return HttpResponse(f'{n1} / {n2} = {n1/n2}')