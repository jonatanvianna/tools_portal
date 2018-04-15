from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'diretivas/$', views.home, name='diretiva_home'),
    url(r'diretivas/abertas/$', views.get_abertas, name='diretiva_abertas'),
    url(r'diretivas/fechadas/$', views.get_fechadas, name='diretiva_fechadas'),
    url(r'diretivas/all/$', views.get_all_diretivas, name='diretiva_all'),
    url(r'diretivas/create/$', views.create, name='create'),
    url(r'diretivas/delete/$', views.delete, name='diretiva_delete'),
    url(r'diretivas/close/$', views.close_diretiva, name='diretiva_close'),
    url(r'diretivas/update/$', views.update, name='diretiva_update')
]