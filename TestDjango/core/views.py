from django.shortcuts import render, redirect
from .models import Agenda
from .forms import CitasForm
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
    # el view sera el responsable de entregar el form al template
    datos = {'form': CitasForm}
    # verificamos que peticion sean post y rescatamos los datos
    if request.method == 'POST':
        # con request recuperamos los datos del formulario
        formulario = CitasForm(request.POST)
        idagenda=request.POST.get("idagenda")
        # validamos el formulario
        if formulario.is_valid:
            if not validaAgenda(idagenda):
                # guardamos en la base de datos
                formulario.save()
                # y mostramos un mensaje
                datos['mensaje'] = "Hora Reservada correctamente"
            else:
                datos['mensaje']="Ya existe un registro asociado a ese codigo "    + idagenda  
    return render(request, 'core/confirmarhora.html', datos)

def validaAgenda(idagenda):
    existe=Agenda.objects.filter(idagenda=idagenda).exists()
    return existe