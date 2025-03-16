
from django.urls import path
from app_cad_usuarios import views
from django.urls import path, include
urlpatterns = [
    path('',views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path("__reload__/", include("django_browser_reload.urls"))
]
