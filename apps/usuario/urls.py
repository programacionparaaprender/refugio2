from django.conf.urls import url

from apps.usuario.views import RegistroUsuario
from apps.usuario.views import UserAPI
from django.contrib.auth.decorators import login_required
from  django.urls import path

urlpatterns = [
	path('registrar', login_required(RegistroUsuario.as_view()), name="registrar"),
	path('api', UserAPI.as_view(), name="api"),
]