# Generated by Django 3.0.7 on 2020-06-27 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cftv', '0003_auto_20200627_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamentocftv',
            name='infra',
            field=models.IntegerField(blank=True, null=True, verbose_name='Distania em metros do Infra vermelho'),
        ),
    ]