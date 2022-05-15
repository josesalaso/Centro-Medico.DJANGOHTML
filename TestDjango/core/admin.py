from django.contrib import admin
from .models import  Espacio, Citas, Gastocomun

# Register your models here.
#permite administarr el modelo completo

admin.site.register(Espacio)
admin.site.register(Citas)
admin.site.register(Gastocomun)


