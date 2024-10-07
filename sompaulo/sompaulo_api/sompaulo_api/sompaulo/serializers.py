from rest_framework import serializers
from .models import Cliente, Venda, Pagamento, Produto, Status, Tipo

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields='__all__'
class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Venda
        fields='__all__'
class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tipo
        fields='__all__'       
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Status
        fields='__all__'
class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pagamento
        fields='__all__'
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Produto
        fields='__all__'
class ProdutoTipoSerializer(serializers.ModelSerializer):
    Tipo = TipoSerializer(many=False, read_only=True)
    class Meta:
        model=Produto
        fields='__all__'
class VendaChaveSerializer(serializers.ModelSerializer):
    Cliente = ClienteSerializer(many=False, read_only=True)
    Status = StatusSerializer(many=False, read_only=True)
    Pagamento = PagamentoSerializer(many=False, read_only=True)
    Produto = ProdutoSerializer(many=False, read_only=True)
    #venda = VendaSerializer(read_only=True)
    class Meta:
        model = Venda
        fields = '__all__'
        depth = 1