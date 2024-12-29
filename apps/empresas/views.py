from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView
from .models import Empresa

# Create your views here.


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['name']


    def form_valid(self, form):  # assim form for validado  preciso fazer pegar obj esta sendo criado
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return httpResponse('ok empresa cadastrada')


class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['name']