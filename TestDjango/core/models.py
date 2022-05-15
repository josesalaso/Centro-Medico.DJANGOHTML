from django.db import models

# Create your models here.
   
#MODELO ESPACIO
class Espacio(models.Model):
    idespacio=models.IntegerField(primary_key=True, verbose_name='ESPACIO ID')
    pago=models.CharField(max_length=50, verbose_name='Pago $')
    horario=models.CharField(null=True, max_length=50, verbose_name='HORARIO DIA/HORA')
    tipoespacio=models.CharField(max_length=50, verbose_name='ESPACIO')
    
    def __str__(self):
        return self.idespacio 
    
#MODELO CITAS ESPACIOS
class Citas(models.Model):
    idespacio=models.IntegerField(primary_key=True, verbose_name='Numero Telefonico')
    run=models.CharField(max_length=50, verbose_name='Rut Residente')  
    hora=models.CharField(max_length=50, verbose_name='Confirmar Hora y Dia Tomada') 
    estado=models.CharField(max_length=50, verbose_name='NOTAS') 
    
    def __str__(self):
        return self.idespacio 
    
#MODELO GASTO COMUN MENSUAL
class Gastocomun(models.Model):
    idgastocomun=models.IntegerField(primary_key=True, verbose_name='GASTO COMUN ID')
    mes=models.CharField(max_length=50, verbose_name='MES') 
    nombreresidente=models.CharField(max_length=50, verbose_name='NOMBRE RESIDENTE') 
    precio=models.IntegerField(verbose_name='Precio $')
    
    def __str__(self):
        return self.idgastocomun



    