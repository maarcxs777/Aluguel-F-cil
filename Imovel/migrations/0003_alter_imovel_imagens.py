# Generated by Django 5.1.2 on 2024-10-22 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Imovel', '0002_remove_imovel_imagem_remove_imovel_titulo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='imagens',
            field=models.ImageField(blank=True, null=True, upload_to='imagens/'),
        ),
    ]
