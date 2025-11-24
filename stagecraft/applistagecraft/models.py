from django.db import models

# Create your models here.

class Offre(models.Model) :

    # Id de l'offre déposé qui est une clé primaire auto-incrémentée
    IdOffre = models.AutoField(primary_key = True)

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
    EtatOffre = models.CharField(max_length = 20, choices = ETATS, default = 'attente')

    # Duree du stage exemple 4 mois chaine de caracteres
    DureeOffre = models.CharField(max_length = 10)

    # Date de début du stage reseignée par le créateur de l'offre (c'est une date)
    DateDebutOffre = models.DateField()

    # Adresse de l'offre de stage (nom de la rue et numéro) chaîne de caratères
    AdresseOffre = models.CharField(max_length = 500)

    # Ville de l'offre de stage, chaîne de caractères
    VilleOffre = models.CharField(max_length = 60)

    # Code postal de l'offre de stage, chaîne de caractères
    CodePostalOffre = models.CharField(max_length = 5)

    # Region de l'offre de stage, chaîne de caractères
    RegionOffre = models.CharField(max_length = 50)

    # Description de l'organisme proposant l'offre de stage, chaîne de caractères
    DescriptionOrganisme = models.CharField(max_length = 10000)











