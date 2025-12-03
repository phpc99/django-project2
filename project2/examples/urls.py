from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.form, name='form'),
    path('questionnaire/', views.questionnaire, name='questionnaire'),
    path('graphs/', views.graphs, name='graphs'),
]