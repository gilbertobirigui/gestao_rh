


# ativar venv  usando bash 
. venv/Scripts/activate



# criando app 
python manage.py startapp nome do app


# configurando o projeto

# projeto principal

settings.py -> registar a app
'apps.empresa',


# app empresa 

models criar os atributos
# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da Empresa')


# criado models
python manage.py makemigrations



# BigAutoField:
  Um campo de incremento automático que cria valores inteiros grandes automaticamente.

# auto_created=True:
  Isso indica que o campo foi criado automaticamente pelo Django, e não foi definido manualmente no modelo.

# primary_key=True:
  Este campo é a chave primária da tabela.

# serialize=False:
  Este campo não será incluído nas representações serializadas do modelo.

# verbose_name='ID':
  Nome legível para o campo no Django Admin ou em outras interfaces.




# agora vamos registrar o models em admin empresa

// admin.py  -> empresa

from django.contrib import admin
from .models import Empresa


admin.site.register(Empresa)



# **************** criando app funcionario ******************

python manage.py startapp funcionario

# 1 - passo 

projeto gestao_rh

# gestao_rh / settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.empresa',
    'apps.funcionario',
]


# funcioario/admin.py

importa o modelo

from .models import Funcionario


registar
admin.site.register(Funcionario)



# python manage.py makemigrations
# python manage.py migrati



# vamos criar um relaciomanto entre tababela

# 1 - funcionario / models.py 

importar biblioteca
from django.contrib.auth.models import User


git rm --cached gestao_rh/__pychace__/ -r



# django static files
https://docs.djangoproject.com/en/5.1/howto/static-files/

