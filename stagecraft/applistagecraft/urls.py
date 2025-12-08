from django.urls import path
from applistagecraft import views

urlpatterns = [
    path('test/', views.test),
    path('offres/', views.offres),
    path('offres/add', views.formulaireCreationOffre),
    path('offres/creerOffre', views.creerOffre),
    path('offres/<int:offre_id>', views.offre),
    path('offres/<int:id_offre>/modifierEtat', views.modifierEtatsOffres),
    path('offres/search/', views.searchOffres),
]