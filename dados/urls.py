from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('verificar_sistema/', views.verificar_sistema, name='verificar_sistema'),
    path('editar_usuario/', views.editar_usuario, name='configurações'),
    path('perfil/', views.perfil, name='perfil'),
]
