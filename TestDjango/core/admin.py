from django.contrib import admin
from .models import Usuario, Agenda, Citas, Pago

# Register your models here.
#permite administarr el modelo completo

admin.site.register(Usuario)
admin.site.register(Agenda)
admin.site.register(Citas)
admin.site.register(Pago)


