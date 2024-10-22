from django.urls import path
from . import views

urlpatterns = [
    path('casas/', views.casas, name='casas')
]
