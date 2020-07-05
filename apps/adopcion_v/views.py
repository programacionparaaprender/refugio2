from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers

#falla en django 2.x
#from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy
# Create your views here.


from apps.adopcion.models import Persona, Solicitud
from apps.adopcion.forms import PersonaForm, SolicitudForm
# Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView 


def index_adopcion(request):
	return HttpResponse('Soy la pagina principal de adopcion')


class SolicitudList(ListView):
	model = Solicitud
	template_name = 'adopcion/solicitud_list.html'


class SolicitudCreate(CreateView):
	model = Solicitud
	template_name = 'adopcion/solicitud_form.html'
	form_class = SolicitudForm
	second_form_class = PersonaForm
	success_url = reverse_lazy('solicitud_listar')
