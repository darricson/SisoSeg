from django.db import models
from cftv.models import Cabo, Fabricante
from django.db.models import Sum, F, FloatField


class CercaOrcamento(models.Model):

    TIPO_CERCA_CHOICES = (

        ('Industrial', 'Industrial'),
        ('Semi-industrial', 'Semi-industrial'),
        ('Convencional', 'Convencional')
    )

    perimetro = models.FloatField('Perimetro')
    elevacao = models.IntegerField('Elevação')
    cantoneira = models.IntegerField('Cantos')
    qtd_isolador = models.IntegerField('Quantidade de isoladores')
    tipo_cerca = models.CharField('Tipo de cerca', max_length=15, choices=TIPO_CERCA_CHOICES, default='Industrial')
    imagem = models.ImageField('Imagem', upload_to='cercas', null=False, blank=False)
    descricao = models.TextField('Descrição', max_length=200, null=False)

    class Meta:

        verbose_name = ' Orçamento Cerca Eletrica'
        verbose_name_plural = 'Orçamento Cercas Eletricas'

    def __str__(self):
        return self.tipo_cerca


class Equipamentocerca(models.Model):

    HASTE_CHOICES = (

        ('Indsutrial 6', 'INDUSTRIAL 6 ISOLADORES'),
        ('SEMI INDUSTRIAL 4', 'SEMI INDUSTRIAL 4 ISOLADORES')
    )

    equipamento_cerca = models.CharField('Equipamento', max_length=100)
    potencia = models.FloatField('Potência', blank=True, null=True)
    metros_linear = models.IntegerField('Distancia doperimetro', blank=True, null=True)
    haste_tipo = models.CharField('Tipo de haste', max_length=29, choices=HASTE_CHOICES, blank=True, null=True)
    tamanho = models.FloatField('Tamanho', blank=True, null=True)
    bitola_arame = models.FloatField('Bitola do fio de aço', null=True, blank=True)
    fabricante = models.ForeignKey(Fabricante, related_name='fabricante', on_delete=models.PROTECT, verbose_name='Fabricante')
    cabo = models.ForeignKey(Cabo, on_delete=models.PROTECT, related_name='cabo', verbose_name='Cabo', null=True, blank=True)

    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'

    def __str__(self):
        return self.equipamento_cerca
