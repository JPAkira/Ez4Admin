from django.urls import path

from apps.index import views
from apps.index.views import index

urlpatterns = [
    path('', index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]