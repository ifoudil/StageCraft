from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.utils import timezone
from datetime import timedelta
from applistagecraft.models import Offre, Candidature

# Create your views here.
def nbOffreRecu(request):
    user = None
    if request.user.is_superuser:
        user = request.user
        
        # On groupe par mois
        donnees = Offre.objects.annotate(
            mois=TruncMonth('DateOffre')
        ).values('mois').annotate(
            total=Count('IdOffre')
        ).order_by('mois')

        labels = []
        data = []

        for entry in donnees:
            if entry['mois']:
                labels.append(entry['mois'].strftime('%B %Y'))
                data.append(entry['total'])

        return render(request, 'applistats/nbOffresRecu.html', {
            'labels': labels, 
            'data': data,
            'user': user
        })
    else:
        return render(request, 'applicompte/login.html')

def propOffreEnCours(request):
    user = None
    if request.user.is_superuser:
        user = request.user

        # On groupe par l'état (via la clé étrangère)
        donnees = Offre.objects.values('EtatOffre__NomEtatsOffres').annotate(
            total=Count('IdOffre')
        ).order_by('total')

        labels = []
        data = []

        for entry in donnees:
            labels.append(entry['EtatOffre__NomEtatsOffres'])
            data.append(entry['total'])

        return render(request, 'applistats/propOffresEnCours.html', {
            'labels': labels, 
            'data': data,
            'user': user
        })
    else:
        return render(request, 'applicompte/login.html')
def nbCandidatureParMois(request):
    user = None
    if request.user.is_superuser:
        user = request.user
        
        # On recule de 365 jours
        date_debut = timezone.now() - timedelta(days=365)

        donnees = Candidature.objects.filter(
            DateCandidature__gte=date_debut
        ).annotate(
            mois=TruncMonth('DateCandidature')
        ).values('mois').annotate(
            total=Count('IdCandidature')
        ).order_by('mois')

        labels = []
        data = []

        for entry in donnees:
            if entry['mois']:
                labels.append(entry['mois'].strftime('%B %Y'))
                data.append(entry['total'])

        return render(request, 'applistats/nbCandidaturesParMois.html', {
            'labels': labels, 
            'data': data,
            'user': user
        })
    else:
        return render(request, 'applicompte/login.html')