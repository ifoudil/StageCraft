from django.contrib import admin

# Register your models here.
from applistagecraft.models import Regions, EtatsOffres, Offre, Departements, Candidature
admin.site.register(Regions)
admin.site.register(EtatsOffres)
admin.site.register(Offre)
admin.site.register(Departements)
admin.site.register(Candidature)