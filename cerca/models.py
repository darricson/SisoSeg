from django.db import models
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
    qtd_isolador = models.IntegerField('Qauntidade de isoladores')
    tipo_cerca = models.CharField('Tipo de cerca', max_length=15, choices=TIPO_CERCA_CHOICES, default='Industrial')
    imagem = models.ImageField('Imagem', upload_to='cercas', null=False)
    descricao = models.TextField('Descrição', max_length=200, null=False)


    class Meta:

        verbose_name = 'Cerca Eletrica'
        verbose_name_plural = 'Cercas Eletricas'

    def __str__(self):
        return self.tipo_cerca
