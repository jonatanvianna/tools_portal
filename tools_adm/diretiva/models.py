# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm


class Diretiva(models.Model):
    # https://docs.djangoproject.com/en/1.11/ref/models/fields/#django.db.models.DateField
    date_entry = models.DateTimeField(auto_now_add=True)  # em prod usar o auto_now_add
    status = models.BooleanField(blank=False, default=False)
    main_ticket = models.TextField(max_length=6, blank=False)
    product = models.CharField(blank=False, max_length=30)
    description = models.TextField(blank=False, max_length=500)
    # https://docs.djangoproject.com/en/1.11/ref/models/fields/#django.db.models.DateField
    date_update = models.DateTimeField(auto_now=True)  # em prod usar o auto_now
    date_closed = models.DateTimeField(null=True)

    class Meta:
        ordering = ['status', 'date_entry']

    def __str__(self):
        return(
            str(self.status),
            str(self.product),
        )


class DiretivaForm(ModelForm):
    class Meta:
        model = Diretiva
        fields = ['id', 'main_ticket', 'product', 'description']
