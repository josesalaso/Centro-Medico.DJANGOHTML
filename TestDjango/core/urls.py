from django.urls import path
from .views import index, reservarhora, registrar, iniciarsesion, contacto, medicos, ubicaciones, anularhora


urlpatterns = [
    path('', index, name="index"),
    path('reservarhora', reservarhora, name="reservarhora"),
    path('registrar', registrar, name="registrar"),
    path('iniciarsesion', iniciarsesion, name="iniciarsesion"),
    path('contacto', contacto, name="contacto"),
    path('medicos', medicos, name="medicos"),
    path('ubicaciones', ubicaciones, name="ubicaciones"),
    path('anularhora', anularhora, name="anularhora"),


]
