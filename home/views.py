from django.shortcuts import render,HttpResponse

def home(request):
    return render(request, 'html/home.html')