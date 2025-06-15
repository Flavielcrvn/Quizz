from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_view, name='quiz'),  # <-- pour l'URL /quiz/
    path('resultat/', views.result_view, name='resultat'),  # si tu envoies ici les résultats
]