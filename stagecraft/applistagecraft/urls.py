from django.urls import path
from applistagecraft import views

urlpatterns = [
    path('homepage/', views.homepage),
    path('offres/', views.offres),
    path('offres/add', views.formulaireCreationOffre),
    path('offres/creerOffre', views.creerOffre),
    path('offres/<int:offre_id>', views.offre),
    path('offres/<int:id_offre>/modifierEtat', views.modifierEtatsOffres),
    path('offres/search/', views.searchOffres),
    path('offres/<int:offre_id>/candidater', views.candidater, name='candidater'),
    path('mes-candidatures/', views.mes_candidatures, name='mes_candidatures'),
    path('offres/en-attente/', views.offresEnAttente),
    path('offres/validees/', views.offresValidees),
    path('offres/refusees/', views.offresRefusees),
    path('offres/cloturees/', views.offresCloturees),
]