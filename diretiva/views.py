# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Diretiva
from .forms import DiretivaForm


def home(request):
    diretiva_list = Diretiva.objects.all()
    paginator = Paginator(diretiva_list, 7)

    user_idc = request.user

    page = request.GET.get('page')
    try:
        diretivas = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        diretivas = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        diretivas = paginator.page(paginator.num_pages)

    context = {'diretivas': diretivas, 'username': user_idc}
    return render(request, 'diretiva/index.html', context)


#@login_required(login_url='/')
def create(request):
    context = {'username': request.user}
    form = DiretivaForm()
    context['form'] = form
    template_name = 'diretiva/nova_diretiva.html'
    if request.method == 'GET':
        return render(request, template_name, context)
    elif request.method == 'POST':
        form = DiretivaForm(request.POST)
        if form.is_valid():

            context['is_valid'] = True
            context['form'] = form
            main_ticket = form.cleaned_data['main_ticket']
            product = form.cleaned_data['product']
            description = form.cleaned_data['description']
            d = Diretiva(
                main_ticket=int(main_ticket),
                product=product,
                description=description
            )
            d.save()
            return render(request, template_name, context)
        else:
            context['form'] = form
            return render(request, template_name, context)


#@login_required(login_url='/')
def update(request):
    context = {'user': request.user}
    template_name = 'diretiva/nova_diretiva.html'
    if request.method == 'GET':
        _id = request.GET.get('id')
        diretiva = Diretiva.objects.get(pk=_id)
        form_data = {
            'id': diretiva.id,
            'main_ticket': diretiva.main_ticket,
            'product': diretiva.product,
            'description': diretiva.description
        }
        form = DiretivaForm(form_data)
        if form.is_valid():
            context['form'] = form
            return render(request, template_name, context)
    if request.method == 'POST':
        _id = request.POST.get('id')
        diretiva = Diretiva.objects.get(pk=_id)
        form = DiretivaForm(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            diretiva.main_ticket = form.cleaned_data['main_ticket']
            diretiva.product = form.cleaned_data['product']
            diretiva.description = form.cleaned_data['description']
            diretiva.save()
            form = DiretivaForm()
            context['form'] = form
            return render(request, template_name, context)
        context['form'] = form
        return render(request, template_name, context)


def delete(request):
    if request.method == 'GET':
        _id = request.GET.get('id')
        deleted = Diretiva.objects.get(pk=_id).delete()
        print(deleted)
    return redirect('diretiva_home')


def close_diretiva(request):
    if request.method == 'GET':
        _id = request.GET.get('id')
        d = Diretiva.objects.get(pk=_id)
        d.status = True
        d.date_closed = datetime.now()
        d.save()
        return redirect('diretiva_home')


def get_all_diretivas(request):
    diretivas = Diretiva.objects.all()
    user_idc = request.user
    context = {'diretivas': diretivas, 'username': user_idc}
    return render(request, 'diretiva/index.html', context)


def get_abertas(request):
    diretivas = Diretiva.objects.filter(status=False)
    user_idc = request.user
    context = {'diretivas': diretivas, 'username': user_idc}
    return render(request, 'diretiva/index.html', context)


def get_fechadas(request):
    diretivas = Diretiva.objects.filter(status=True)
    user_idc = request.user
    context = {'diretivas': diretivas, 'username': user_idc}
    return render(request, 'diretiva/index.html', context)
