from django.db import models

# Create your models here.

class factura(models.Model):
	
	fecha = models.DateField(auto_now = True)
	hora = models.DateTimeField()
	Nombre = models.CharField(max_length = 25)
	Apellido = models.CharField(max_length = 25)
	Cedula = models.IntegerField()
	Producto = models.CharField(max_length = 10)
	Cantidad_por_pesada = models.IntegerField()
	precio_actual = models.FloatField()
	total_pagar = models.FloatField()

class Facturador(models.Model):
	ID_usuario = models.CharField(max_length = 25)
	ID_clave = models.CharField(max_length = 25)
	Nombre = models.CharField(max_length = 25)
	Apellido = models.CharField(max_length = 25)

class precio(models.Model):
	platanos = models.FloatField(unique = True)