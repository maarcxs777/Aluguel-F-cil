from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Imovel.urls')),
    path('', include('dados.urls')),
    path('', include('home.urls')),
    path('', include('casas.urls')),
    path('', include('contatos.urls')),
    path('', include('sobre.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)