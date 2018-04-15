from django.shortcuts import render

# Create your views here.

from django.views.generic.base import TemplateView


class DashBoardTemplateView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(DashBoardTemplateView, self).get_context_data(**kwargs)
        context['title'] = "About US"
        return context
