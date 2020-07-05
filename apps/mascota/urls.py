from django.conf.urls import url, include

from  django.urls import path

from django.contrib.auth.decorators import login_required
from apps.mascota.views import MascotaList, MascotaCreate

from apps.mascota.views import listadousuarios 
from apps.mascota.views import index
from apps.mascota.views import mascota_view, mascota_list
from apps.mascota.views import mascota_edit, mascota_delete 
from apps.mascota.views import MascotaUpdate, MascotaDelete 

urlpatterns = [
    path('', index, name='index'),
    path('nuevo', login_required(MascotaCreate.as_view()), name='mascota_crear'),
    path(r'^listar', login_required(MascotaList.as_view()), name='mascota_listar'), 
    path('editar/<int:pk>/', login_required(MascotaUpdate.as_view()), name='mascota_editar'),
    path('eliminar/<int:pk>/', login_required(MascotaDelete.as_view()), name='mascota_eliminar'),
    path('listado', listadousuarios, name="listado"), 
]


""" url(r'^editar/(?P<pk>\d+)/$', login_required(MascotaUpdate.as_view()), name='mascota_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(MascotaDelete.as_view()), name='mascota_eliminar'), """

""" app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
] """
