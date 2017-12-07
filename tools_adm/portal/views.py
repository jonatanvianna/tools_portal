# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_screen(request):
    #controla o method usado, pois no primeiro carregamento sempre
    #deve ser GET.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'portal/login.html',{'user': user})
    else:
        return render(request, 'portal/login.html')

#@login_required
def home(request):
    return render(request, 'portal/home.html', {'username': request.user})

@login_required
def logout_portal(request):
    logout(request)
    return redirect('login_screen')
