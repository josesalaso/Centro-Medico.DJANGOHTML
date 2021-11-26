from django.db import models

# Create your models here.
#MODELO USUARIO
class Usuario(models.Model):
    run=models.CharField(max_length=10, primary_key=True, verbose_name='Rut')
    nombre=models.CharField(max_length=20, verbose_name='Nombre')
    email=models.CharField(max_length=50, verbose_name='Email')
    contraseña=models.CharField(max_length=50, verbose_name='Contraseña')
    tipo=models.CharField(max_length=50, verbose_name='Tipousuario')
    def __str__(self):
        return self.run
    
#MODELO AGENDA_MEDICO
class Agenda(models.Model):
    idagenda=models.IntegerField(primary_key=True, verbose_name='Id Agenda')
    hora=models.CharField(max_length=50, verbose_name='Hora')
    medicoespecialidad=models.CharField(null=True, max_length=50, verbose_name='Medico y especialidad')
    run=models.CharField(max_length=10, verbose_name='Rut Medico')
    
    def __str__(self):
        return self.idagenda 
    
#MODELO CITAS_PACIENTE
class Citas(models.Model):
    idagenda=models.IntegerField(primary_key=True, verbose_name='Numero Telefonico')
    run=models.CharField(max_length=10, verbose_name='Rut Medico')  
    hora=models.CharField(max_length=50, verbose_name='Hora') 
    estado=models.CharField(max_length=50, verbose_name='NOTAS') 
    
    def __str__(self):
        return self.idagenda 
    
#MODELO PAGO
class Pago(models.Model):
    idpago=models.IntegerField(primary_key=True, verbose_name='Id pago')
    run=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comprobante=models.CharField(max_length=50, verbose_name='Comprobante')
    precio=models.IntegerField(verbose_name='Precio')
    
    def __str__(self):
        return self.run
    
#MODELO INFORME
class Informes(models.Model):
    idinforme=models.IntegerField(primary_key=True, verbose_name='Id informe')
    idpago=models.ForeignKey(Pago, on_delete=models.CASCADE)
    tipoinforme=models.CharField(max_length=50, verbose_name='tipo informe')
    
    def __str__(self):
        return self.idinforme 