from django import forms
from django.forms import ModelForm
from applistagecraft.models import Offre

class OffreForm(forms.ModelForm) :
    class Meta :
        model = Offre
        fields = [
            'OrganismeOffre', 
            'IntituleOffre', 
            'NomContact', 
            'PrenomContact', 
            'MailContact', 
            'DescriptionOrganisme', 
            'DetailsOffre', 
            'DureeOffre', 
            'DateDebutStage', 
            'AdresseOffre',
            'VilleOffre',
            'CodePostalOffre',
            'RegionOffre', ]
        labels = {
            'OrganismeOffre': 'Organisme',
            'IntituleOffre': 'Titre du stage',
            'NomContact': 'Nom',
            'PrenomContact': 'Prénom',
            'MailContact': 'Mail',
            'DescriptionOrganisme': 'Description de l\'entreprise',
            'DetailsOffre': 'Description du stage',
            'DureeOffre': 'Durée du stage',
            'DateDebutStage': 'Date de début du stage',
            'AdresseOffre': 'Adresse',
            'VilleOffre': 'Ville',
            'CodePostalOffre': 'Code Postal',
            'RegionOffre': 'Région',
        }