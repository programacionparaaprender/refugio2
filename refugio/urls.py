"""refugio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, reverse_lazy
from django.conf.urls import url, include
#from django.contrib.auth.views import login
from django.contrib.auth import login
from django.contrib.auth.views import logout_then_login
#from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
#from django.contrib.auth.views import password_reset_done
#from django.contrib.auth.views import password_reset_confirm
#from django.contrib.auth.views import password_reset_complete
from django.contrib.auth.views import LoginView
#from django.contrib.auth.views import password_reset, password_reset_done,password_reset_confirm,password_reset_complete
#from .views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

dic_1 =  {
'template_name':'registration/password_reset_form.html',
'email_template_name': 'registration/password_reset_email.html'
}
dic_2 =  {
'template_name': 'registration/password_reset_done.html'
}
dic_3 =  {
'template_name': 'registration/password_reset_confirm.html'
}
dic_4 = {
'template_name': 'registration/password_reset_complete.html'
}


""" from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_done
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_complete """


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mascota/', include('apps.mascota.urls')),
    url(r'^adopcion/', include('apps.adopcion.urls')),
    url(r'^logout/', logout_then_login, name='logout'),
    #url(r'^mascota/', include('apps.mascota.urls', namespace='mascota')),
    #url(r'^admin/', admin.site.urls),
    #url(r'^mascota/', include('apps.mascota.urls', namespace='mascota')),
    #url(r'^adopcion/', include('apps.adopcion.urls', namespace='adopcion')),
    url(r'^usuario/', include('apps.usuario.urls')),
    #url(r'^accounts/login/', login, {'template_name':'index.html'}, name='login'),
    url(r'^accounts/login/', LoginView.as_view(template_name='index.html'), name='login'),
    path('reset/password_reset', PasswordResetView.as_view(), dic_1, name='password_reset'), 
    path('password_reset_done', PasswordResetDoneView.as_view(), dic_2, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), dic_3,name='password_reset_confirm'),
    path('reset/done', PasswordResetCompleteView.as_view(), dic_4,name='password_reset_complete'),
]

    #url(r'^logout/', logout_then_login, name='logout'),
    #url(r'^reset/password_reset', password_reset, dic_1, name='password_reset'), 
    #url(r'^password_reset_done', password_reset_done, dic_2, name='password_reset_done'),
    #url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, dic_3,name='password_reset_confirm'),
    #url(r'^reset/done', password_reset_complete, dic_4,name='password_reset_complete'),