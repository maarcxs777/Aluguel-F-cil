# Generated by Django 5.1.2 on 2024-10-22 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Imovel', '0007_remove_imovel_endereco'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imovel',
            name='descricao',
        ),
    ]
