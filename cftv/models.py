import uuid
from django.db import models
from cliente.models import Cliente
from stdimage.models import StdImageField


# metodo que pega o arquivo de imagem, separa a extnsa0 e recria com um novo nome
# uuid faz a geração aleatoria do nome do arquivo de imagem
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class CftvOrcamento(models.Model):

    AMBIENTE_CHOICES = (

        ('Interno', 'Interno'),
        ('Semi-aberto', 'Semi-aberto'),
        ('Externo', 'Externo'),
        ('Abertura', 'Abertura')
    )

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name='CLiente')
    ambiente = models.CharField('Ambiente', max_length=15, choices=AMBIENTE_CHOICES)
    imagem = models.ImageField('Imagem do local', upload_to='media')
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


class Equipamentocftv(models.Model):
    equipamento_cftv = models.CharField('Equipamento', max_length=100)
    fabricante = models.ForeignKey(Fabricante, related_name='fabricante_fabricante', on_delete=models.PROTECT, verbose_name='Fabricante')
    modelo = models.CharField('Modelo', max_length=100)
    infra = models.IntegerField('Distania em metros do Infra vermelho', blank=True, null=True)
    lente = models.FloatField('Tamanho da lente', blank=True, null=True)
    consumo_amper = models.FloatField('Consumo em amperes', blank=True, null=True)
    consumo_volts = models.FloatField('Consumo em volts', blank=True, null=True)
    canais = models.IntegerField('Quantidade de canais', blank=True, null=True)
    armazenamento = models.IntegerField('Quantidade de armazenamento em terabyte', blank=True, null=True)

    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'

    def __str__(self):
        return self.equipamento_cftv
