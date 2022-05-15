from django.shortcuts import render, redirect
from .models import Espacio, Citas, Gastocomun
from .forms import EspacioForm, CitasForm, GastocomunForm
# Create your views here.

def index(request):
    return render(request, 'core/index.html')
def interfazadministradorcondominio(request):
    return render(request, 'core/interfazadministradorcondominio.html')
def interfazdirectiva(request):
    return render(request, 'core/interfazdirectiva.html')
def interfazconcerje(request):
    return render(request, 'core/interfazconcerje.html')

def reservarhora(request):
    # accediendo al objeto que contiene los datos de la base de datos
    # el metodo all traera todas las horas que estan en la tabla
    espacio = Espacio.objects.all()
    # ahora crearemos una variable que le pase los datos del producto al template
    datos = {
        'espacio': espacio
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
        idespacio=request.POST.get("idespacio")
        # validamos el formulario
        if formulario.is_valid:
            if not validaEspacio(idespacio):
                # guardamos en la base de datos
                formulario.save()
                # y mostramos un mensaje
                datos['mensaje'] = "Hora Reservada correctamente"
            else:
                datos['mensaje']="Ya existe un registro asociado a ese codigo "    + idespacio  
    return render(request, 'core/confirmarhora.html', datos)

def validaEspacio(idespacio):
    existe=Espacio.objects.filter(idespacio=idespacio).exists()
    return existe

def pagaranularhora(request):
        # accediendo al objeto que contiene los datos de la base de datos
    # el metodo all traera todos los productos que estan en la tabla
    citas = Citas.objects.all()
    # ahora crearemos una variable que le pase los datos del producto al template
    datos = {
        'citas': citas
    }
    # ahora lo agregamos para que se envie al templateee
    return render(request, 'core/pagaranularhora.html', datos)

def delhora(request,id):
    #el id es el identificador de la tabla productos
    #buscando los datos en la base de datos
    citas=Citas.objects.get(idespacio=id)
    #eliminamos el producto del id buscado
    citas.delete()
    #ahora redirigmos a la pagina con el listado
    return redirect(to="pagaranularhora")

def agregargastocomunmensual(request):
    # el view sera el responsable de entregar el form al template
    datos = {'form': GastocomunForm}
    # verificamos que peticion sean post y rescatamos los datos
    if request.method == 'POST':
        # con request recuperamos los datos del formulario
        formulario = GastocomunForm(request.POST)
        idgastocomun=request.POST.get("idgastocomun")
        # validamos el formulario
        if formulario.is_valid:
            if not validaGastocomun(idgastocomun):
                # guardamos en la base de datos
                formulario.save()
                # y mostramos un mensaje
                datos['mensaje'] = "AGREGADO correctamente correctamente"
            else:
                datos['mensaje']="Ya existe un registro asociado a ese codigo "    + idgastocomun  
    return render(request, 'core/agregargastocomunmensual.html', datos)

def validaGastocomun(idgastocomun):
    existe=Gastocomun.objects.filter(idgastocomun=idgastocomun).exists()
    return existe


def gastocomun(request):
    # accediendo al objeto que contiene los datos de la base de datos
    # el metodo all traera todas las horas que estan en la tabla
    gastocomun = Gastocomun.objects.all()
    # ahora crearemos una variable que le pase los datos del producto al template
    datos = {
        'gastocomun': gastocomun
    }
    # ahora lo agregamos para que se envie al templateee
    return render(request, 'core/gastocomun.html', datos)



def agregarespacio(request):
    # el view sera el responsable de entregar el form al template
    datos = {'form': EspacioForm}
    # verificamos que peticion sean post y rescatamos los datos
    if request.method == 'POST':
        # con request recuperamos los datos del formulario
        formulario = EspacioForm(request.POST)
        idespacio=request.POST.get("idespacio")
        # validamos el formulario
        if formulario.is_valid:
            if not validaEspacio(idespacio):
                # guardamos en la base de datos
                formulario.save()
                # y mostramos un mensaje
                datos['mensaje'] = "Guardado correctamente"
            else:
                datos['mensaje']="Ya existe un registro asociado a ese codigo"    + idespacio  
    return render(request, 'core/agregarespacio.html', datos)




