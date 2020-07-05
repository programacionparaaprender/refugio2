from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers

#falla en django 2.x
#from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy

#from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


from django.views.generic.list import ListView 


from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota

def index(request):
	return render(request, 'mascota/index.html')


class MascotaList(ListView):
	model = Mascota
	template_name = 'mascota/mascota_list.html'
	paginate_by = 2


class MascotaCreate(CreateView):
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/mascota_form.html'
	#reverse_lazy
	success_url = reverse_lazy('mascota_listar')


def listadousuarios(request):
    lista = serializers.serialize('json', User.objects.all(), fields=['username', 'first_name','password'])
    return HttpResponse(lista, content_type='application/json')


def mascota_view(request):
	if request.method == 'POST':
		form = MascotaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index')
	else:
		form = MascotaForm()
	return render(request, 'mascota/mascota_form.html',{'form':form})


def mascota_list(request):
	mascota = Mascota.objects.all().order_by('id')
	contexto = {'mascotas':mascota}
	return render(request, 'mascota/mascota_list.html', contexto)


def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota_listar')
    return render(request, 'mascota/mascota_form.html', {'form':form})


def mascota_delete(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'POST':
		mascota.delete()
		return redirect('mascota_listar')
	return render(request, 'mascota/mascota_delete.html', {'mascota':mascota})




class MascotaUpdate(UpdateView):
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/mascota_form.html'
	#reverse_lazy
	success_url = reverse_lazy('mascota_listar')


class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'mascota/mascota_delete.html'
	#reverse_lazy
    success_url = reverse_lazy('mascota_listar') 



