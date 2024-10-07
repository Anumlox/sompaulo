from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
class Pagamento(models.Model):
    forma = models.CharField(max_length=100)
    def __str__(self):
        return self.forma
class Tipo(models.Model):
    nome_tipo = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_tipo
class Status(models.Model):
    status = models.CharField(max_length=100)
    def __str__(self):
        return self.status
class Produto(models.Model):
    idTipo = models.ForeignKey(Tipo, on_delete=models.CASCADE) 
    nome_produto = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    quantidade = models.IntegerField()
    foto = models.CharField(max_length=250)
    foto2 = models.CharField(max_length=250)
    def __str__(self):
        return self.idTipo
class Venda(models.Model):
    idStatus = models.ForeignKey(Status, on_delete=models.CASCADE)
    idPagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE)
    idProduto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)    
    data_venda = models.DateField()
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.idCliente 