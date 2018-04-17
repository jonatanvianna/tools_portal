from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='pdm_home'),
    url(r'^resultado/$', views.busca_log, name='busca_log'),
]
