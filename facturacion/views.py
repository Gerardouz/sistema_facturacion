from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from facturacion.models import Facturador

def login(request):
	
	facturador = Facturador.objects.all()
	my_login = loader.get_template("login.html")
	mi_context = Context({'facturador':facturador})
	return HttpResponse(my_login.render(mi_context))
def bienvenido(request):
	facturador = Facturador.objects.all()
	html = "<html><body>Bienvenido {{facturador.Nombre</body></html>"
	return HttpResponse(html)




	"""
	administrador = login_administrador.objects.all()
	html = loader.get_template("bienvenido.html")
	context = Context({'administrador':administrador})
	return HttpResponse(html.render(context))
	"""