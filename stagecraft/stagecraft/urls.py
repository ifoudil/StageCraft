"""
URL configuration for stagecraft project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from applistagecraft import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test),
    path('offres/', views.offres),
    path('offres/add', views.formulaireCreationOffre),
    path('offres/creerOffre', views.creerOffre),
    path('offres/<int:offre_id>', views.offre),
    path('offres/<int:id_offre>/modifierEtat', views.modifierEtatsOffres),
    path('offres/search/', views.searchOffres),
]
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('applistagecraft.urls')),
#     path('', include('applicompte.urls')),

# ]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
