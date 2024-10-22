from django.db import models

class Imovel(models.Model):
    imagens = models.ImageField(upload_to='imagens/', null=True, blank=True)  # Permite que o campo seja nulo
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255, default='Endereço não informado')
    descricao = models.TextField(default='Descrição não fornecida')

    def __str__(self):
        return self.nome
