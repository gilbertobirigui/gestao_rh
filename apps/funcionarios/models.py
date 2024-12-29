from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa

# Create your models here.

class Funcionario(models.Model):
    name = models.CharField(max_length=60, verbose_name= 'nome')
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete = models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name
