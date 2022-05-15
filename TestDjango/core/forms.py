from django import forms
from django.forms import ModelForm
from .models import Espacio
from .models import Citas
from .models import Gastocomun



class CitasForm(ModelForm):
    class Meta:
        model = Citas
        fields =["idespacio", "run", "hora", "estado"]
        
class GastocomunForm(ModelForm):
    class Meta:
        model = Gastocomun
        fields =["idgastocomun", "mes", "nombreresidente", "precio"]    
        
        
        
class EspacioForm(ModelForm):
    class Meta:
        model = Espacio
        fields =["idespacio", "pago", "horario", "tipoespacio"]  
        
                  