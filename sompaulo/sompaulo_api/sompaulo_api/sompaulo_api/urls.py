"""
URL configuration for cardapio_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#importa a lista e os detalhes do arquivo views
from sompaulo.views import produto_list, produto_detail, produto_list_tipo, cliente_list, tipo_list, status_list, pagamento_list, venda_list, venda_list_cliente, produto_list_tipo
urlpatterns = [
    path('admin/', admin.site.urls),
    path('produto/', produto_list),
    path('produto/<int:pk>/', produto_detail),
    path('produto/<str:idTipo>/', produto_list_tipo),
    path('venda/', venda_list),
    path('venda/<int:idCliente>/', venda_list_cliente),
    path('cliete/', cliente_list),
    path('tipo/', tipo_list),
    path('status/', status_list),
    path('pagamento/', pagamento_list)
]   
