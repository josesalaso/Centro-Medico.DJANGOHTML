from django.shortcuts import render, redirect
from .models import Agenda, Citas, Pago
from .forms import CitasForm, PagoForm
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
def secretaria(request):
    return render(request, 'core/secretaria.html')

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

def anularhora(request):
        # accediendo al objeto que contiene los datos de la base de datos
    # el metodo all traera todos los productos que estan en la tabla
    citas = Citas.objects.all()
    # ahora crearemos una variable que le pase los datos del producto al template
    datos = {
        'citas': citas
    }
    # ahora lo agregamos para que se envie al templateee
    return render(request, 'core/anularhora.html', datos)

def delhora(request,id):
    #el id es el identificador de la tabla productos
    #buscando los datos en la base de datos
    citas=Citas.objects.get(idagenda=id)
    #eliminamos el producto del id buscado
    citas.delete()
    #ahora redirigmos a la pagina con el listado
    return redirect(to="anularhora")

def cajeropagar(request):
    # el view sera el responsable de entregar el form al template
    datos = {'form': PagoForm}
    # verificamos que peticion sean post y rescatamos los datos
    if request.method == 'POST':
        # con request recuperamos los datos del formulario
        formulario = PagoForm(request.POST)
        idpago=request.POST.get("idpago")
        # validamos el formulario
        if formulario.is_valid:
            if not validaPago(idpago):
                # guardamos en la base de datos
                formulario.save()
                # y mostramos un mensaje
                datos['mensaje'] = "Pagado correctamente correctamente"
            else:
                datos['mensaje']="Ya existe un registro asociado a ese codigo "    + idpago  
    return render(request, 'core/cajeropagar.html', datos)

def validaPago(idpago):
    existe=Pago.objects.filter(idpago=idpago).exists()
    return existe


def comprobantepago(request):
    # accediendo al objeto que contiene los datos de la base de datos
    # el metodo all traera todas las horas que estan en la tabla
    pago = Pago.objects.all()
    # ahora crearemos una variable que le pase los datos del producto al template
    datos = {
        'pago': pago
    }
    # ahora lo agregamos para que se envie al templateee
    return render(request, 'core/comprobantepago.html', datos)



def form_producto(request):
    # el view sera el responsable de entregar el form al template
    datos = {'form': ProductoForm}
    # verificamos que peticion sean post y rescatamos los datos
    if request.method == 'POST':
        # con request recuperamos los datos del formulario
        formulario = ProductoForm(request.POST)
        cod_producto=request.POST.get("cod_producto")
        # validamos el formulario
        if formulario.is_valid:
            if not validaProducto(cod_producto):
                # guardamos en la base de datos
                formulario.save()
                # y mostramos un mensaje
                datos['mensaje'] = "Guardado correctamente"
            else:
                datos['mensaje']="Ya existe un registro asociado a ese codigo"    + cod_producto  
    return render(request, 'core/form_producto.html', datos)

def validaProducto(cod_producto):
    existe=Producto.objects.filter(cod_producto=cod_producto).exists()
    return existe

def form_mod_producto(request, id):

    # el id es el identificador de la tabla productos
    # buscando los datos en la base de datos
    # buscamos por codigo que llega como dato en la url
    productos = Producto.objects.get(cod_producto=id)
    # ahora le entregamos los datos del producto al formulario
    datos = {'form': ProductoForm(instance=productos)}

    # verificamos que la peticion sean post y rescatamos los datos
    if request.method == 'POST':
        # con request recuperamos los datos del formulario y le agregamos el id modificar
        formulario = ProductoForm(data=request.POST, instance=productos)
        # validamos el formulario
        if formulario.is_valid:
            # ahora guardamosen la base datos
            formulario.save()
            # enviamos mensaje
            datos['mensaje'] = "Modificado Correctamente"

    return render(request, 'core/form_mod_producto.html', datos)




def form_del_producto(request,id):
    #el id es el identificador de la tabla productos
    #buscando los datos en la base de datos
    productos=Producto.objects.get(cod_producto=id)
    #eliminamos el producto del id buscado
    productos.delete()
    #ahora redirigmos a la pagina con el listado
    return redirect(to="listado")