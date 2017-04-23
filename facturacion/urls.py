from django.conf.urls import *
from facturacion.views import *

urlpatterns = [
	url(r'^$', login),
	url(r'^bienvenido/',bienvenido),
    
]