from django.urls import path
from . import views
urlpatterns = [
    path('imovel/', views.imovel, name='imovel')
]
