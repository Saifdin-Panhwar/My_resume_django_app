from pipes import Template
from django.shortcuts import render,HttpResponse
from django.views.generic.base import TemplateView
# Create your views here.
class myview(TemplateView):
    template_name = 'index.html'