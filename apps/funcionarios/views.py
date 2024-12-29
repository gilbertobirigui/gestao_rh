
from django.views.generic import ListView, UpdateView, DeleteView
from .models import Funcionario
from django.urls import reverse_lazy


class FuncionariosList(ListView):
    model = Funcionario
    context_object_name = 'funcionarios'
    
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa if hasattr(self.request.user, 'funcionario') else None
        if empresa_logada:
            queryset = Funcionario.objects.filter(empresa=empresa_logada)
        else:
            queryset = Funcionario.objects.none()  # Retorna um queryset vazio se o usuário não tiver um funcionário associado
        return queryset

class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['name', 'departamentos']


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')

