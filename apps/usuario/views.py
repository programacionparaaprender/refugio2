from django.shortcuts import render

import json
from rest_framework.views import APIView
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy


from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView 
from apps.usuario.forms import RegistroForm
from apps.usuario.serializers import UserSerializer

class RegistroUsuario(CreateView):
	model = User
	template_name = "usuario/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('mascota_listar')
""" class MascotaCreate(CreateView):
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/mascota_form.html'
	#reverse_lazy
	success_url = reverse_lazy('mascota_listar') """

class UserAPI(APIView):
	serializer = UserSerializer
	
	def get(self, request, format=None):
		lista = User.objects.all()
		response = self.serializer(lista, many=True)
		return HttpResponse(json.dumps(response.data), content_type='application/json')




