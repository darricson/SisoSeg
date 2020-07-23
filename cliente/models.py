from django.db import models


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=30)
    email = models.EmailField('E-mail', max_length=60)
    telefone = models.CharField('Telefone', max_length=12)
    rua = models.CharField('Rua', max_length=50)
    numero = models.CharField('Numero/Quadra/Lote', max_length=5)
    bairro = models.CharField('Bairro', max_length=50)
    cidade = models.CharField('Cidade', max_length=50)
    ponto_referencia = models.CharField('Ponto de referencia', max_length=100)

    class Meta:
        verbose_name = 'CLiente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome
