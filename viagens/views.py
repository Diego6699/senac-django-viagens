from django import views
from django import forms
from django.shortcuts import render
from django.template import Origin
from viagens.forms import ViagemForms

# Create your views here.

def index(request):
    form = ViagemForms()
    contexto = {'form':form}
    return render(request ,'index.html',contexto)
'''
def revConsulta(request):
    if request.method == 'POST':
        form = ViagemForms(request.POST)
        contexto = {'form' : form}
        return render(request, 'consulta.html',contexto) 
'''
        
def revConsulta(request):
    if request.method == 'POST':
        form = ViagemForms(request.POST)
        if form.is_valid():
            contexto = {'form':form}#erro
            return render(request,'consulta.html',contexto)
        else:
            print('form inválido')
            contexto = {'form':form}
            return render(request,'index.html',contexto)
