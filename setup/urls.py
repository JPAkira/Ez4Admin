from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


handler404 = 'setup.default.view_404'

urlpatterns = [
    path('', include('index.urls')),
    path('', include('clientes.urls')),
    path('', include('estoque.urls')),
    path('', include('vendas.urls')),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
