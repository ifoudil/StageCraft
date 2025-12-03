from django.shortcuts import render

# Importation des modeles
from applistagecraft.models import Offre, EtatsOffres
from applistagecraft.forms import OffreForm

# Create your views here.

def test(request):
    return render(
        request,
        'applistagecraft/test.html',
    )

def offres(request) :

    # Récupération des offres de la base de données
    lesOffres = Offre.objects.all()
    lesEtats = EtatsOffres.objects.all()

    # retourne emplacement du template offres.html et calcul des offres sous forme de dictionnaire python
    return render(
        request,
        'applistagecraft/offres.html',
        {
            'offres': lesOffres,
            'etats': lesEtats
        }
    )

def formulaireCreationOffre(request) :
    form = OffreForm

    # Retrour de l'emplacement du template de creation d'offre
    return render(
        request,
        'applistagecraft/formulaireCreationOffre.html',
        {'form' : form}
    )

def creerOffre(request) :

    form = OffreForm(request.POST, request.FILES)
    print(form.errors.as_json())
    if form.is_valid() :
        intitule = form.cleaned_data['IntituleOffre']
        print(intitule)
        form.save()

    return render(
        request,
        'applistagecraft/traitementFormulaireCreationOffre.html',
        {"IntituleOffre": intitule},
    )

def offre(request, offre_id) :

    # Récupération des offres de la base de données
    lOffre = Offre.objects.get(IdOffre = offre_id)
    
    # retourne emplacement du template offres.html et calcul des offres sous forme de dictionnaire python
    return render(
        request,
        'applistagecraft/offre.html',
        {'offre': lOffre}
    )

def etatsOffres(request, etat_id):
    etat = EtatsOffres.objects.get(IdEtatsOffres = etat_id)

    return render(request, "mon_template.html", {
        "etats": etats,
        "offr": offr
    })

