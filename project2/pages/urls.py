from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # sem redicionamento vai para a home, ou seja, pagina inicial
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]