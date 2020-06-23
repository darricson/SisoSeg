from django.db import models


class CftvOrcamento(models.Model):

    AMBIENTE_CHOICES = (

        ('Interno', 'Interno'),
        ('Externo', 'Externo')
    )

    ambiente = models.CharField('Ambiente', max_length=10, choices=AMBIENTE_CHOICES)
    imagem = models.ImageField('Imagem do local', upload_to='local')
    local = models.CharField('Local', max_length=80)
    descricao = models.TextField('Descrição do local', max_length=200)


    class Meta:

        verbose_name = 'Orçamento CFTV'
        verbose_name_plural = 'Orçamentos CFTV'

    def __str__(self):
        return self.local


class Fabricante(models.Model):
    nome = models.CharField('Fabricante', max_length=100)

    class Meta:
        verbose_name = 'Fabricante'
        verbose_name_plural = 'Fabricantes'

    def __str__(self):
        return self.nome


class Cabo(models.Model):
    modelo = models.CharField('Modelo', max_length=100)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.PROTECT, verbose_name='Fabricante')
    bitolas = models.FloatField('Bitola')
    aplicacao = models.CharField('Aplicação', max_length=50)

    class Meta:
        verbose_name = 'Cabo'
        verbose_name_plural = 'Cabos'

    def __str__(self):
        return self.modelo


class Equipamento(models.Model):
    equipamento = models.CharField('Equipamento', max_length=100)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.PROTECT, verbose_name='Fabricante')
    modelo = models.CharField('Modelo', max_length=100)
    infra = models.IntegerField('Distania do Infra vermelho')
    lente = models.FloatField('Tamanho da lente')
    consumo_amper = models.FloatField('Consumo em amperes')
    consumo_volts = models.FloatField('Consumo em volts')
    canais = models.IntegerField('Quantidade de canais')
    armazenamento = models.IntegerField('Quantidade de armazenamento em terabyte')


    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'

    def __str__(self):
        return self.equipamento
