# Generated by Django 3.0.7 on 2020-07-30 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cftv', '0010_auto_20200729_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cftvorcamento',
            name='imagem',
            field=models.ImageField(upload_to='media', verbose_name='Imagem do local'),
        ),
    ]