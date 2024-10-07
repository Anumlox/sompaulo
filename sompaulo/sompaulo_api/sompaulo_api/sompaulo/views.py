#imports necessarios para o controller
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cliente, Venda, Status, Produto, Pagamento, Tipo
from .serializers import ClienteSerializer, VendaSerializer, VendaChaveSerializer, TipoSerializer, PagamentoSerializer, ProdutoSerializer, StatusSerializer, ProdutoTipoSerializer

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def produto_list(request):
    #caso o metodo seja get traz a lista de todos os pratos
    if request.method=='GET':
            produto = Produto.objects.all()
            serializer = ProdutoSerializer(produto, many=True)
            return Response(serializer.data)
    #caso o metodo seja post, valida e cria um novo prato
    elif request.method=='POST':
        serializer = ProdutoSerializer(data=request.data)
        #verifica se os dados recebidos são validos
        if serializer.is_valid():
            #caso valido, salva no banco o novo item do cardapio
            produto = serializer.save()
            #resposta de sucesso no cadastro
            response_data={
                'message': 'Produto cadastrado com sucesso',
                'data': serializer.data,
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)
#requisicoes para consultar detalhe, alterar e apagar produto
@api_view(['GET', 'PUT', 'DELETE'])
def produto_detail(request, pk):
    try:
        produto = Produto.objects.get(pk=pk)
    except Produto.DoesNotExist:
        return Response({'Erro':'Produto não encontrado'},
                        status=404)
    #traz os detalhes do prato consultado com get
    if request.method=='GET':
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)
    #faz a alteração no prato
    elif request.method=='PUT':
        serializer = ProdutoSerializer(produto, 
                                        data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data={
                'message':'Produto alterado com sucesso',
                'data': serializer.data,
            }
            return Response(response_data)    
        return Response(serializer.errors, status=400)
    #apaga o prato do banco de dados
    elif request.method=='DELETE':
        produto.delete();
        return Response({'message':'Produto excluído com sucesso'},
                        status=204)
#lista de pratos por categoria
@api_view(['GET'])
def produto_list(request):
    #caso o metodo seja get traz a lista de todos os pratos
    if request.method=='GET':
            
            produtos = Produto.objects.all()
            serializer = ProdutoSerializer(produtos, many=True)
            return Response(serializer.data)
#lista geral de vendas
@api_view(['GET'])
def venda_list(request):
      #caso o metodo seja get traz a lista de todos os pratos
    if request.method=='GET':
            
            vendas = Venda.objects.all()
            serializer = VendaSerializer(vendas, many=True)
            return Response(serializer.data)
@api_view(['GET'])
def cliente_list(request):
      #caso o metodo seja get traz a lista de todos os pratos
    if request.method=='GET':
            
            clientes = Cliente.objects.all()
            serializer = ClienteSerializer(clientes, many=True)
            return Response(serializer.data)
@api_view(['GET'])
def tipo_list(request):
      #caso o metodo seja get traz a lista de todos os pratos
    if request.method=='GET':
            
            tipos = Tipo.objects.all()
            serializer = TipoSerializer(tipos, many=True)
            return Response(serializer.data)
@api_view(['GET'])
def status_list(request):
      #caso o metodo seja get traz a lista de todos os pratos
    if request.method=='GET':
            
            statuss = Status.objects.all()
            serializer = StatusSerializer(statuss, many=True)
            return Response(serializer.data)
@api_view(['GET'])
def pagamento_list(request):
      #caso o metodo seja get traz a lista de todos os pratos
    if request.method=='GET':
            
            pagamentos = Pagamento.objects.all()
            serializer = PagamentoSerializer(pagamentos, many=True)
            return Response(serializer.data)
    #caso o metodo seja post, valida e cria um novo prato
#lista de vendas por prato
@api_view(['GET'])
def venda_list_cliente(request, idCliente):
      #caso o metodo seja get traz a lista de todos os pratos
    if request.method=='GET':
            #cardapio = Cardapio.objects.get(pk=idPrato)
            #vendas  = cardapio.pratos.all()
            vendas = Venda.objects.filter(idCliente=idCliente)
            serializer = VendaChaveSerializer(vendas, many=True)
            return Response(serializer.data)
    #caso o metodo seja post, valida e cria um novo prato
@api_view(['GET'])
def produto_list_tipo(request, idTipo):
      #caso o metodo seja get traz a lista de todos os pratos
    if request.method=='GET':
            #cardapio = Cardapio.objects.get(pk=idPrato)
            #vendas  = cardapio.pratos.all()
            produtos = Produto.objects.filter(idTipo=idTipo)
            serializer = ProdutoTipoSerializer(produtos, many=True)
            return Response(serializer.data)
