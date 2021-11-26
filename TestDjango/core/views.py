from django.shortcuts import render, redirect


# Create your views here.

def reservarhora(request):
    return render(request, 'core/reservarhora.html')
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