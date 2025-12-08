from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your models here.
class Regions(models.Model) :

    # Id de la région incrémenté automatiquement
    IdRegion = models.AutoField(primary_key = True)

    # Le nom de la region est une chaine de caractères
    NomRegion = models.CharField(max_length = 50)

    def __str__(self) -> str :
        return self.NomRegion

class EtatsOffres(models.Model) :

    # Id de l'état'
    IdEtatsOffres = models.AutoField(primary_key = True)

    # Le nom de l'état
    NomEtatsOffres = models.CharField(max_length = 50)

    def __str__(self) -> str :
        return self.NomEtatsOffres

class Offre(models.Model) :

    # Id de l'offre déposé qui est une clé primaire auto-incrémentée
    IdOffre = models.AutoField(primary_key = True)

    # Logo de l'entreprise proposant l'offre
    ImageOffre = models.ImageField(default = 'imagesEntreprises/default.png', upload_to = 'imagesEntreprises')

    # Le nom de l'organisme proposant l'offre est une chaine de caractères
    OrganismeOffre = models.CharField(max_length = 50)

    # Le nom du contact pour l'offre est une chaine de caractères
    NomContact = models.CharField(max_length = 50)

    # Le prénom du contact pour l'offre est une chaine de caractères
    PrenomContact = models.CharField(max_length = 50)

    # Le mail du contact pour l'offre est une chaine de caractères
    MailContact = models.CharField(max_length = 80)

    # Intitulé de l'offre de stage est une chaine de caractères
    IntituleOffre = models.CharField(max_length = 50)

    # Date du dépôt de l'offre de stage est la date actuelle (pas affichée dans le formulaire de création d'une offre)
    DateOffre = models.DateTimeField(auto_now_add = True)

    # Détails sur l'offre avec par exemple les missions du stage, chaîne de caractères
    DetailsOffre = models.CharField(max_length = 10000)

    # Etat possible (pas affiché dans le formulaire de création)
    ETATS = [
        ('attente', 'En attente de validation'),
        ('validee', 'Validée'),
        ('Refusee', 'Refusée'),
        ('Cloturee', 'Cloturée')
    ]

    # Etat de l'offre mis automatiquement à en attente et chaine de de caractères
    EtatOffre = models.ForeignKey(EtatsOffres,on_delete=models.CASCADE, default=1)

    # Duree du stage exemple 4 mois chaine de caracteres
    DureeOffre = models.CharField(max_length = 10)

    # Date de début du stage reseignée par le créateur de l'offre (c'est une date)
    DateDebutStage = models.DateField()

    # Adresse de l'offre de stage (nom de la rue et numéro) chaîne de caratères
    AdresseOffre = models.CharField(max_length = 500)

    # Ville de l'offre de stage, chaîne de caractères
    VilleOffre = models.CharField(max_length = 60)

    # Code postal de l'offre de stage, chaîne de caractères
    CodePostalOffre = models.CharField(max_length = 5)

    # Region de l'offre de stage, selectionnée parmis les regions existante du modele
    RegionOffre = models.ForeignKey(Regions,on_delete=models.CASCADE)

    # Description de l'organisme proposant l'offre de stage, chaîne de caractères
    DescriptionOrganisme = models.CharField(max_length = 10000)

    def __str__(self) -> str :
        return self.IntituleOffre + '(posté par' + self.OrganismeOffre + ')'


class Departements(models.Model) :

    # Id de la région
    IdDepartement = models.AutoField(primary_key = True)

    # Le nom de la region est une chaine de caractères
    NomDepartement = models.CharField(max_length = 50)

    # Le nom de la region est une chaine de caractères
    CodeDepartement = models.CharField(max_length = 5)

    def __str__(self) -> str :
        return self.CodeDepartement + ' : ' + self.NomDepartement

class Candidature(models.Model):
    IdCandidature = models.AutoField(primary_key=True)
    Etudiant = models.ForeignKey(User, on_delete=models.CASCADE)
    Offre = models.ForeignKey(Offre, on_delete=models.CASCADE)
    DateCandidature = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Candidature de {self.Etudiant.username} pour {self.Offre.IntituleOffre}"











