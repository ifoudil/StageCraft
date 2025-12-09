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
    user = None
    
    if request.user.is_authenticated:
        user = request.user

        # Récupération des offres de la base de données
        lesOffres = Offre.objects.all()
        lesEtats = EtatsOffres.objects.all()

        # retourne emplacement du template offres.html et calcul des offres sous forme de dictionnaire python
        return render(
            request,
            'applistagecraft/offres.html',
            {
                'offres': lesOffres,
                'etats': lesEtats,
                'user': user
            }
        )
    else:
        return render(
            request,
            'applicompte/login.html',
        )

def formulaireCreationOffre(request) :

    user = None

    if not request.user.is_authenticated:
        form = OffreForm

        # Retrour de l'emplacement du template de creation d'offre
        return render(
            request,
            'applistagecraft/formulaireCreationOffre.html',
            {'form' : form}
        )
    
    else:
        user = request.user

        # Récupération des offres de la base de données
        lesOffres = Offre.objects.all()
        lesEtats = EtatsOffres.objects.all()

        # retourne emplacement du template offres.html et calcul des offres sous forme de dictionnaire python
        return render(
            request,
            'applistagecraft/offres.html',
            {
                'offres': lesOffres,
                'etats': lesEtats,
                'user': user,
            }
        )


def creerOffre(request) :
    user = None

    if not request.user.is_authenticated:
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

    else:
        user = request.user

        # Récupération des offres de la base de données
        lesOffres = Offre.objects.all()
        lesEtats = EtatsOffres.objects.all()

        # retourne emplacement du template offres.html et calcul des offres sous forme de dictionnaire python
        return render(
            request,
            'applistagecraft/offres.html',
            {
                'offres': lesOffres,
                'etats': lesEtats,
                'user': user
            }
        )


def offre(request, offre_id) :
    user = None

    if request.user.is_authenticated:
        user = request.user

        # Récupération de l'offre
        lOffre = Offre.objects.get(IdOffre = offre_id)
        
        # On compte combien de candidatures existent pour cette offre
        nb_candidats = Candidature.objects.filter(Offre=lOffre).count()
        
        # On calcule le reste (5 places max)
        places_restantes = 5 - nb_candidats
        return render(
            request,
            'applistagecraft/offre.html',
            {
                'offre': lOffre,
                'places_restantes': places_restantes,
                'user': user
            }
        )
    
    else:
        return render(
            request,
            'applicompte/login.html',
        )

def modifierEtatsOffres(request, id_offre):
    user = None

    if request.user.is_staff:
        user = request.user
        if request.method == "POST":
            id_etat = request.POST.get("etat")

            offre = Offre.objects.get(IdOffre=id_offre)
            offre.EtatOffre_id = id_etat
            offre.save()

            return render(
                request, 
                "applistagecraft/traitementFormulaireEtat.html", 
                {
                    "offre": offre,
                    "user": user
                }
            )
        
    elif request.user.is_authenticated:
        user = request.user
        # Récupération des offres de la base de données
        lesOffres = Offre.objects.all()
        lesEtats = EtatsOffres.objects.all()

        # retourne emplacement du template offres.html et calcul des offres sous forme de dictionnaire python
        return render(
            request,
            'applistagecraft/offres.html',
            {
                'offres': lesOffres,
                'etats': lesEtats,
                'user': user
            }
        )
    
    else:
        return render(
            request,
            'applicompte/login.html'
        )


def searchOffres(request) :
    user = None
    if request.user.is_authenticated:
        user = request.user

        info = request.POST.get('search')
        lesOffres = Offre.objects.filter(OrganismeOffre__contains=info) | Offre.objects.filter(IntituleOffre__contains=info)

        lesEtats = EtatsOffres.objects.all()

        return render(
            request,
            'applistagecraft/offres.html',
            {
                'offres': lesOffres,
                'etats': lesEtats,
                'user': user
            }
        )
    
    else:
        return render(
            request,
            'applicompte/login.html'
        )

def candidater(request, offre_id):
    user = None

    if request.user.is_authenticated and not request.user.is_staff:
        user = request.user
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
                    'etats': lesEtats,
                    'user': user
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
                'etats': lesEtats,
                'user': user
            }
        )
    
    elif request.user.is_staff:
        user = request.user
        lesOffres = Offre.objects.all()
        lesEtats = EtatsOffres.objects.all()
        # Redirection vers la page des offres
        return render(
            request,
            'applistagecraft/offres.html',
            {
                'offres': lesOffres,
                'etats': lesEtats,
                'user': user
            }
        )

    else:
        return render(
            request,
            'applicompte/login.html'
        )


def mes_candidatures(request):
    user = None

    if request.user.is_authenticated and not request.user.is_staff:
        user = request.user
        # On récupère les candidatures de l'étudiant connecté
        candidatures = Candidature.objects.filter(Etudiant=request.user)
        
        return render(
            request, 
            'applistagecraft/mes_candidatures.html', 
            {
                'candidatures': candidatures,
                'user': user
            }
        )
    
    elif request.user.is_staff:
        user = request.user

        lesOffres = Offre.objects.all()
        lesEtats = EtatsOffres.objects.all()
        # Redirection vers la page des offres
        return render(
            request,
            'applistagecraft/offres.html',
            {
                'offres': lesOffres,
                'etats': lesEtats,
                'user': user
            }
        )

    else:
        return render(
            request,
            'applicompte/login.html'
        )

def offresEnAttente(request):
    user = None

    if request.user.is_staff :
        lesOffres = Offre.objects.filter(EtatOffre__NomEtatsOffres="En attente de validation")
        lesEtats = EtatsOffres.objects.all()
        user = request.user

        return render(request, 'applistagecraft/offres.html', {
            'offres': lesOffres,
            'etats': lesEtats,
            'user': user
        })
    elif request.user.is_authenticated :
        lesOffres = Offre.objects.all()
        lesEtats = EtatsOffres.objects.all()
        user = request.user

        return render(request, 'applistagecraft/offres.html', {
            'offres': lesOffres,
            'etats': lesEtats,
            'user': user
        })
    else :
        return render(request, 'applicompte/login.html')

def offresValidees(request):
    user = None

    if request.user.is_superuser :
        lesOffres = Offre.objects.filter(EtatOffre__NomEtatsOffres="Validée")
        lesEtats = EtatsOffres.objects.all()
        user = request.user

        return render(request, 'applistagecraft/offres.html', {
            'offres': lesOffres,
            'etats': lesEtats,
            'user': user
        })
    elif request.user.is_authenticated :
        lesOffres = Offre.objects.all()
        lesEtats = EtatsOffres.objects.all()
        user = request.user

        return render(request, 'applistagecraft/offres.html', {
            'offres': lesOffres,
            'etats': lesEtats,
            'user': user
        })
    else :
        return render(request, 'applicompte/login.html')

def offresRefusees(request):
    user = None

    if request.user.is_superuser :
        lesOffres = Offre.objects.filter(EtatOffre__NomEtatsOffres="Refusée")
        lesEtats = EtatsOffres.objects.all()
        user = request.user

        return render(request, 'applistagecraft/offres.html', {
            'offres': lesOffres,
            'etats': lesEtats,
            'user': user
        })
    elif request.user.is_authenticated :
        lesOffres = Offre.objects.all()
        lesEtats = EtatsOffres.objects.all()
        user = request.user

        return render(request, 'applistagecraft/offres.html', {
            'offres': lesOffres,
            'etats': lesEtats,
            'user': user
        })
    else :
        return render(request, 'applicompte/login.html')

def offresCloturees(request):
    user = None

    if request.user.is_superuser :
        lesOffres = Offre.objects.filter(EtatOffre__NomEtatsOffres="Cloturée")
        lesEtats = EtatsOffres.objects.all()
        user = request.user

        return render(request, 'applistagecraft/offres.html', {
            'offres': lesOffres,
            'etats': lesEtats,
            'user': user
        })
    elif request.user.is_authenticated :
        lesOffres = Offre.objects.all()
        lesEtats = EtatsOffres.objects.all()
        user = request.user

        return render(request, 'applistagecraft/offres.html', {
            'offres': lesOffres,
            'etats': lesEtats,
            'user': user
        })
    else :
        return render(request, 'applicompte/login.html')