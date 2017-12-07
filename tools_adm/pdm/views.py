# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import subprocess


@login_required
def home(request):
    return render(request, 'pdm/index.html',  {'username':request.user})


@csrf_exempt
def busca_log(request):
    context = {'user_idc': request.user}

    id_perm = request.POST.get('id_perm')
    user = request.POST.get('user')

    list_log = []
    subprocess.call(['perda_de_mensagens', id_perm, user])
    with open('/tmp/' + user + '_relatorio_final.txt') as r:
        for line in r:
            list_log.append(line)

    context['lista'] = list_log
    return render(request, 'pdm/resposta.html', context)
