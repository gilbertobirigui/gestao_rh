
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('apps.core.urls')),     # quando a pessoa nao digitar nao ele vai pra core. tela principal
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('empresa/', include('apps.empresas.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
 
]


