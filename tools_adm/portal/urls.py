from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.login_screen, name='login_screen'),
    # url(r'^autentica/$', views.autentica, name='autentica'),
    url(r'^home/$', views.home, name='home'),
    url(r'^logout_portal/$', views.logout_portal, name='logout_portal'),
]
