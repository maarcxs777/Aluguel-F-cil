# Generated by Django 5.1.2 on 2024-10-22 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Imovel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imovel',
            name='imagem',
        ),
        migrations.RemoveField(
            model_name='imovel',
            name='titulo',
        ),
        migrations.AddField(
            model_name='imovel',
            name='imagens',
            field=models.ImageField(default=2, upload_to='imagens/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imovel',
            name='endereco',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='telefone',
            field=models.CharField(max_length=15),
        ),
    ]