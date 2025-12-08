from django.shortcuts import render

# Importation des modeles
from applistagecraft.models import Offre, EtatsOffres, Candidature
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

# def offre(request, offre_id) :

#     # Récupération des offres de la base de données
#     lOffre = Offre.objects.get(IdOffre = offre_id)
    
#     # retourne emplacement du template offres.html et calcul des offres sous forme de dictionnaire python
#     return render(
#         request,
#         'applistagecraft/offre.html',
#         {'offre': lOffre}
#     )



def offre(request, offre_id) :
    # Récupération de l'offre
    lOffre = Offre.objects.get(IdOffre = offre_id)
    
    # --- AJOUT DU CALCUL ---
    # On compte combien de candidatures existent pour cette offre
    nb_candidats = Candidature.objects.filter(Offre=lOffre).count()
    
    # On calcule le reste (5 places max)
    places_restantes = 5 - nb_candidats
    # -----------------------

    return render(
        request,
        'applistagecraft/offre.html',
        {
            'offre': lOffre,
            'places_restantes': places_restantes  # On passe la variable au template
        }
    )

def modifierEtatsOffres(request, id_offre):

    if request.method == "POST":
        id_etat = request.POST.get("etat")  # valeur du SELECT

        offre = Offre.objects.get(IdOffre=id_offre)
        offre.EtatOffre_id = id_etat        # si ForeignKey
        offre.save()

        return render(
            request, 
            "applistagecraft/traitementFormulaireEtat.html", 
            {"offre": offre}
        )


def searchOffres(request) :
    info = request.POST.get('search')
    lesOffres = Offre.objects.filter(OrganismeOffre__contains=info) | Offre.objects.filter(IntituleOffre__contains=info)

    lesEtats = EtatsOffres.objects.all()

    return render(
        request,
        'applistagecraft/offres.html',
        {
            'offres': lesOffres,
            'etats': lesEtats
        }
    )

def candidater(request, offre_id):
    # On récupère l'offre avec la méthode standard get()
    # Note : Si l'ID n'existe pas, cela renverra une erreur 500 (Offre.DoesNotExist), 
    # ce qui est le comportement standard sans get_object_or_404.
    lOffre = Offre.objects.get(IdOffre=offre_id)

    lesOffres = Offre.objects.all()
    lesEtats = EtatsOffres.objects.all()

    # Vérifier si l'étudiant a déjà candidaté
    deja_candidat = Candidature.objects.filter(Offre=lOffre, Etudiant=request.user).exists()

    if deja_candidat:
        # Redirection simple vers la liste si déjà candidat
        return render(
            request,
            'applistagecraft/offres.html',
            {
                'offres': lesOffres,
                'etats': lesEtats
            }
        )

    # Compter les candidatures existantes
    nb_candidats = Candidature.objects.filter(Offre=lOffre).count()

    if nb_candidats < 5:
        # Créer la candidature
        Candidature.objects.create(Etudiant=request.user, Offre=lOffre)

        # Vérifier si on atteint le quota (4 + 1 = 5)
        if nb_candidats + 1 >= 5:
            # Récupérer l'état Cloturee (on suppose qu'il existe ou on le crée)
            etat_cloture, created = EtatsOffres.objects.get_or_create(NomEtatsOffres="Cloturee")
            lOffre.EtatOffre = etat_cloture
            lOffre.save()

    # Redirection vers la page des offres
    return render(
        request,
        'applistagecraft/offres.html',
        {
            'offres': lesOffres,
            'etats': lesEtats
        }

    )