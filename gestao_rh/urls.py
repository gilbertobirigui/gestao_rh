
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.core.urls')),     # quando a pessoa nao digitar nao ele vai pra core. tela principal
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('admin/', admin.site.urls),
]
