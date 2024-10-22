from django.shortcuts import render, HttpResponse
from PIL import Image
import os
from django.conf import settings
from .models import Imovel

def imovel(request):
    if request.method == "GET":
        return render(request, 'html/imovel.html')
    elif request.method == "POST":
        imagens = request.FILES.get('my_file')
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')
        descricao = request.POST.get('descricao')

        imovel = Imovel(imagens=imagens, nome=nome, email=email, telefone=telefone, endereco=endereco, descricao=descricao)
        imovel.save()

        return HttpResponse('Cadastro realizado com sucesso')
