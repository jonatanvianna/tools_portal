# -*- coding=utf-8 -*-
from django import forms
from django.core.validators import RegexValidator


class DiretivaForm(forms.Form):
    id = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput(),
        label=''
    )
    main_ticket = forms.IntegerField(
        validators=[RegexValidator(regex=r'^\d{6}$', message="O ticket deve ter 6 digitos", code='ivalid')],
        label="Ticket Principal",
        help_text="Número do Ticket principal",
        error_messages={'required': 'Please enter the ticket'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: 278596'
            }
        )
    )
    product = forms.CharField(
        # validators=[RegexValidator(regex=r'[ab]', message="erro karay", code='ivalid')],
        label="Produto", max_length=15,
        help_text="Adicione uma informação sucinta como email, app1, app2 ou app3, por exemplo.",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: App1'
            }
        )
    )
    description = forms.CharField(
        label="Descrição",
        help_text="Descrição da diretiva. Ex.: Problemas com App1, não escalonar. Realizar a investigação e repassar ao N2.",
        max_length=500,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '...'
            }
        )
    )
