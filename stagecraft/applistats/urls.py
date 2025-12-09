from django.urls import path
from applistats import views

urlpatterns = [
    path('stats/offres-recues/', views.nbOffreRecu, name='nbOffreRecu'),
    path('stats/repartition-etats/', views.propOffreEnCours, name='propOffreEnCours'),
    path('stats/candidatures/', views.nbCandidatureParMois, name='nbCandidatureParMois'),
]