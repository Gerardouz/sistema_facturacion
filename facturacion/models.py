from django.db import models

# Create your models here.

class factura(models.Model):
	ID_Factura = models.AutoField(primary_key = True)
	fecha = models.DateField(auto_now = True)
	hora = models.DateTimeField()
	Nombre = models.CharField(max_length = 25)
	Apellido = models.CharField(max_length = 25)
	Cedula = models.IntegerField()
	Producto = models.CharField(max_length = 10)
	Cantidad_por_pesada = models.IntegerField()
	precio_actual = models.FloatField()
	total_pagar = models.FloatField()

class login_administrador(models.Model):
	ID_usuario_adm = models.CharField(max_length = 25)
	ID_clave_adm = models.CharField(max_length = 25)

class login_facturador(models.Model):
	ID_usuario_facturador = models.CharField(max_length = 25)
	ID_clave_facturador = models.CharField(max_length = 25)
	Nombre_del_facturador = models.CharField(max_length = 25)
	Apellido_del_facturador = models.CharField(max_length = 25)

class precio(models.Model):
	ID_precio = models.FloatField()