from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from facturacion.models import login_administrador, login_facturador

def login(request):
	administrador = login_administrador.objects.all()
	facturador = login_facturador.objects.all()
	my_login = loader.get_template("login.html")
	mi_context = Context({'administrador':administrador})
	return HttpResponse(my_login.render(mi_context))
def bienvenido(request):
	administrador = login_administrador.objects.all()
	my_loader = loader.get_template("bienvenido.html")
	context = Context({'administrador':administrador})
	return HttpResponse(my_loader.render(context))