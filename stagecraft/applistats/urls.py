from django.urls import path
from applistats import views

urlpatterns = [
    path('stats/offres-recues/', views.nbOffreRecu, name='nbOffreRecu'),
]