from django.shortcuts import render,HttpResponse

def sobre(request):
    return render(request, 'html/sobre.html')