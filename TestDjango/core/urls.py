from django.urls import path
from .views import index, reservarhora, registrar, iniciarsesion, contacto, medicos, ubicaciones, anularhora, confirmarhora, delhora, cajeropagar, comprobantepago, secretaria, modificaragendamedico


urlpatterns = [
    path('', index, name="index"),
    path('reservarhora', reservarhora, name="reservarhora"),
    path('registrar', registrar, name="registrar"),
    path('iniciarsesion', iniciarsesion, name="iniciarsesion"),
    path('contacto', contacto, name="contacto"),
    path('medicos', medicos, name="medicos"),
    path('ubicaciones', ubicaciones, name="ubicaciones"),
    path('confirmarhora', confirmarhora, name="confirmarhora"),
    path('anularhora', anularhora, name="anularhora"),
    path('anularhora/<id>', anularhora, name="anularhora"),
    path('delhora/<id>', delhora, name="delhora"),
    path('cajeropagar', cajeropagar, name="cajeropagar"),
    path('comprobantepago', comprobantepago, name="comprobantepago"),
    path('secretaria', secretaria, name="secretaria"),
    path('modificaragendamedico', modificaragendamedico, name="modificaragendamedico"),

]
