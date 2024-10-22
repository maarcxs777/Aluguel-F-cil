from django.shortcuts import render, HttpResponse
from .models import Parceiro

def parceiro(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        # Salvando no banco de dados
        parceiro = Parceiro(nome=nome, email=email, telefone=telefone)
        parceiro.save()

        return render(request, 'html/clique_aqui.html')
    else:
        return render(request, 'html/contatos.html')
