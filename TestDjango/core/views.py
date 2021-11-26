from django.shortcuts import render, redirect
from .models import Agenda

# Create your views here.

def index(request):
    return render(request, 'core/index.html')
def registrar(request):
    return render(request, 'core/registrar.html')
def iniciarsesion(request):
    return render(request, 'core/iniciarsesion.html')
def contacto(request):
    return render(request, 'core/contacto.html')
def medicos(request):
    return render(request, 'core/medicos.html')
def ubicaciones(request):
    return render(request, 'core/ubicaciones.html')
def anularhora(request):
    return render(request, 'core/anularhora.html')

def reservarhora(request):
    # accediendo al objeto que contiene los datos de la base de datos
    # el metodo all traera todas las horas que estan en la tabla
    agenda = Agenda.objects.all()
    # ahora crearemos una variable que le pase los datos del producto al template
    datos = {
        'agenda': agenda
    }
    # ahora lo agregamos para que se envie al templateee
    return render(request, 'core/reservarhora.html', datos)
def confirmarhora(request):
    return render(request, 'core/confirmarhora.html')