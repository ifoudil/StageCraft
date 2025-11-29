from django import forms
from django.forms import ModelForm
from applistagecraft.models import Offre, Regions

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

        widgets = {
            'OrganismeOffre': forms.TextInput(attrs={
                'placeholder': "Nom de l'entreprise"
            }),
            'IntituleOffre': forms.TextInput(attrs={
                'placeholder': "Intitulé de l'offre de stage"
            }),
            'NomContact': forms.TextInput(attrs={
                'placeholder': "Nom du contact entreprise"
            }),
            'PrenomContact': forms.TextInput(attrs={
                'placeholder': "Prenom du contact entreprise"
            }),
            'MailContact': forms.TextInput(attrs={
                'placeholder': "Mail du contact entreprise",
                'type': "email"
            }),
            'DescriptionOrganisme': forms.TextInput(attrs={
                'placeholder': "Description de l'entreprise"
            }),
            'DetailsOffre': forms.TextInput(attrs={
                'placeholder': "Détails de l'offre de stage"
            }),
            'DureeOffre': forms.TextInput(attrs={
                'placeholder': "Durée du stage"
            }),
            'DateDebutStage': forms.TextInput(attrs={
                'placeholder': "Date de début du stage",
                'type': "date"
            }),
            'AdresseOffre': forms.TextInput(attrs={
                'placeholder': "Adresse du lieu de stage"
            }),
            'VilleOffre': forms.TextInput(attrs={
                'placeholder': "Ville du lieu de stage"
            }),
            'CodePostalOffre': forms.TextInput(attrs={
                'placeholder': "Code postal du lieu de stage"
            }),
            'RegionOffre': forms.Select(),
        }