from django.shortcuts import render,HttpResponse

def casas(request):
    return render(request, 'html/casas.html')