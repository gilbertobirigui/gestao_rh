
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.funcionarios.models import Funcionario


@login_required
def home(request):

    # quero pegar o funcionario para ver se ta logado

    # criar um dicionario data

    data = {}
    data['usuario'] = request.user
    return render(request, 'core/index.html', data)

