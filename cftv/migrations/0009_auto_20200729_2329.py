# Generated by Django 3.0.7 on 2020-07-30 02:29

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('cftv', '0008_auto_20200729_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cftvorcamento',
            name='imagem',
            field=stdimage.models.StdImageField(upload_to='media/local', verbose_name='Imagem do local'),
        ),
    ]