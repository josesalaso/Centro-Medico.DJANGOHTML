from django import forms
from django.forms import ModelForm
from .models import Usuario
from .models import Agenda
from .models import Citas
from .models import Pago



class CitasForm(ModelForm):
    class Meta:
        model = Citas
        fields =["idagenda", "run", "hora", "estado"]
        
class PagoForm(ModelForm):
    class Meta:
        model = Pago
        fields =["idpago", "run", "nombrecliente", "precio"]        