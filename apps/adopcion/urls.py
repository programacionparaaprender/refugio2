from django.conf.urls import url, include
#from django.urls import path
from apps.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete
from  django.urls import path
urlpatterns = [
    path('', index_adopcion, name='index'),
    path('solicitud/listar', SolicitudList.as_view(), name='solicitud_listar'),
    path('solicitud/nueva', SolicitudCreate.as_view(), name='solicitud_crear'),
    path('solicitud/editar/<int:pk>/', SolicitudUpdate.as_view(), name='solicitud_editar'),
    path('solicitud/eliminar/<int:pk>/', SolicitudDelete.as_view(), name='solicitud_eliminar'), 
]

"""     
    
    path('', index, name='index'),
    path('nuevo', login_required(MascotaCreate.as_view()), name='mascota_crear'),
    path(r'^listar', login_required(MascotaList.as_view()), name='mascota_listar'), 
    path('editar/<int:pk>/', login_required(MascotaUpdate.as_view()), name='mascota_editar'),
    path('eliminar/<int:pk>/', login_required(MascotaDelete.as_view()), name='mascota_eliminar'),
    path(r'^listado', listadousuarios, name="listado"), 
    
    """