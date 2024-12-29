from django.db import models
from django.urls import reverse


class Empresa(models.Model):
    name = models.CharField(max_length=100, help_text='Nome da Empresa', verbose_name='nome', default='Default Name')



    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse('home')
    