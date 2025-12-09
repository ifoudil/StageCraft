from django import forms
from django.forms import ModelForm
from applistagecraft.models import Offre, Regions

class OffreForm(forms.ModelForm) :
    class Meta :
        model = Offre
        fields = [
            'ImageOffre', 
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
            'ImageOffre': 'Logo de l\'Entreprise', 
            'OrganismeOffre': 'Nom de l\'Entreprise',
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
            'IntituleOffre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Ex: Développeur Full Stack Python/Django"
            }),
            'DetailsOffre': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Détaillez les missions, les compétences requises, etc.",
                'rows': 5
            }),
            'DureeOffre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Ex: 6 mois"
            }),
            'DateDebutStage': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'OrganismeOffre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Nom de votre société"
            }),
            'DescriptionOrganisme': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Présentez votre structure en quelques lignes...",
                'rows': 3
            }),
            'ImageOffre': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'AdresseOffre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Numéro et nom de rue"
            }),
            'VilleOffre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Ville"
            }),
            'CodePostalOffre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Code Postal"
            }),
            'RegionOffre': forms.Select(attrs={
                'class': 'form-select'
            }),
            'NomContact': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Nom"
            }),
            'PrenomContact': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Prénom"
            }),
            'MailContact': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "exemple@entreprise.com"
            }),
        }