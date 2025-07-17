from django import forms
from django import forms
from django.core.validators import RegexValidator
from .models import Domaine, Source, Collecteur

from django import forms
class BaseCollecteForm(forms.Form):
    username = forms.CharField(
        label="Login",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        }),
        required=True
    )

class PeriodiqueForm(BaseCollecteForm):
    pass

class MonographieForm(BaseCollecteForm):
    pass

class IndexeurForm(BaseCollecteForm):
    pass

class IndexationControleForm(BaseCollecteForm):
    pass

class PriseDeVueForm(BaseCollecteForm):
    pass

#Ce formulaire fait reference a la partie de rechecrche par titre de controle dans periodique

class SearchFormPeriodique(forms.Form):
    query = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'search-input',
            'placeholder': 'Rechercher par titre de controle',
        })
    )
DOMAINE_CHOICES = [
    ('Individu - Culture - Société', 'Individu - Culture - Société'),
    ('Droit - Politique', 'Droit - Politique'),
    ('Economie - Finances', 'Economie - Finances'),
    ('Travail - Prévoyance', 'Travail - Prévoyance'),
    ('Aménagement - Environnement', 'Aménagement - Environnement'),
    ('Mines', 'Mines'),
    ('Toponymie administrative du Maroc', 'Toponymie administrative du Maroc'),
    ('Activités Economiques', 'Activités Economiques'),
    ('Elevage - Pêches', 'Elevage - Pêches'),
    ('Agriculture - Forêts', 'Agriculture - Forêts'),
    ('Terre-Cosmos', 'Terre-Cosmos'),
    ('Organisations - Opérations', 'Organisations - Opérations'),
    ('Noms de personnes', 'Noms de personnes'),
    ('Mathématique', 'Mathématique'),
    ('Sciences biologiques', 'Sciences biologiques'),
    ('Informatique', 'Informatique'),
    ('Toponymie géophysique et géopolitique du monde', 'Toponymie géophysique et géopolitique du monde'),
    ('Bâtiment - Construction', 'Bâtiment - Construction'),
    ('Mesure-Analyse', 'Mesure-Analyse'),
    ('Chimie', 'Chimie'),
    ('Physique', 'Physique'),
    ('Matériaux - Produits', 'Matériaux - Produits'),
    ('Noms de lieux du Maroc', 'Noms de lieux du Maroc'),
    ('Science médicale', 'Science médicale'),
    ('Technologie', 'Technologie'),
    ('Electrotechnique', 'Electrotechnique'),
    ('Télécommunication', 'Télécommunication'),
    ('Groupements - Confréries', 'Groupements - Confréries'),
    ('Taxonomie animale', 'Taxonomie animale'),
    ('Bassins hydrologiques et oueds du Maroc', 'Bassins hydrologiques et oueds du Maroc'),
    ('Machines', 'Machines'),
    ('Dynasties', 'Dynasties'),
]

LANGUE_CHOICES = [
    ('Fr', 'Français'),
    ('En','Anglais'),
    ('Ar','Arabe'),
    ('Sp','Espagnol'),
    ('De','Allemand'),
    # ajoute d'autres options ici
]

SOURCE_CHOICES = [
    ('', '— Sélectionner —'),
    ('src1', 'Source 1'),
    ('src2', 'Source 2'),
]

TYPE_ACQUISITION_CHOICES = [
    ('', '— Sélectionner —'),
    ('type1', 'Type 1'),
    ('type2', 'Type 2'),
]


class PeriodiqueFormGeneral(forms.Form):
    isbn = forms.CharField(
        label="N° Enregistrement",
        max_length=12,
        widget=forms.TextInput(attrs={'size': '30', 'class': 'form-control'}),
        required=False,
        help_text="/2003"
    )

    stitre = forms.CharField(
        label="Titre Article *",
        max_length=255,
        widget=forms.TextInput(attrs={'size': '100', 'class': 'form-control'}),
    )

    auteur = forms.CharField(
        label="Auteur / Collectivité",
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'size': '100', 'class': 'form-control'}),
        help_text="Séparer les auteurs par des virgules / si plusieurs",
    )

    titre = forms.CharField(
        label="Titre Source **",
        max_length=255,
        widget=forms.TextInput(attrs={'size': '100', 'class': 'form-control'}),
    )

    vol = forms.CharField(
        label="Volume",
        max_length=25,
        required=False,
        widget=forms.TextInput(attrs={'size': '10', 'class': 'form-control'}),
    )
    tom = forms.CharField(
        label="Tome",
        max_length=25,
        required=False,
        widget=forms.TextInput(attrs={'size': '10', 'class': 'form-control'}),
    )
    num = forms.CharField(
        label="Numéro",
        max_length=25,
        required=False,
        widget=forms.TextInput(attrs={'size': '10', 'class': 'form-control'}),
    )

    dat_edit = forms.DateField(
        label="Date d'édition",
        required=False,
        widget=forms.TextInput( attrs={'size': '10', 'placeholder': 'YYYY-MM-DD', 'class': 'form-control'}),
        input_formats=['%Y-%m-%d'],
    )
    pages = forms.CharField(
        label="Pagination",
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={'size': '30', 'class': 'form-control'}),
        help_text="ex: 20‑25",
    )

    critere = forms.ChoiceField(
        label="Domaine",
        choices=DOMAINE_CHOICES,
        initial='-1',
         widget=forms.Select(attrs={
            'class': 'form-control',  # Classe Bootstrap (optionnelle)
            'style': 'width: 62%; padding: 8px; border-radius: 5px; border: none; height: 40px',
    })
    )

    lang = forms.ChoiceField(
        label="Langue",
        choices=LANGUE_CHOICES,
        initial  = 'Fr',
        widget=forms.Select(attrs={
            'class': 'form-control',  # Classe Bootstrap (optionnelle)
            'style': 'width: 62%; padding: 8px; border-radius: 5px; border: none; height: 40px',
    })
    )
    
    src = forms.ChoiceField(
        label="Source Expéditrice",
        choices=SOURCE_CHOICES,
        required=False,
         widget=forms.Select(attrs={
            'class': 'form-control',  # Classe Bootstrap (optionnelle)
            'style': 'width: 62%; padding: 8px; border-radius: 5px; border: none; height: 40px',
    })
    )

    type = forms.ChoiceField(
        label="Type d'acquisition",
        choices=TYPE_ACQUISITION_CHOICES,
        required=False,
         widget=forms.Select(attrs={
            'class': 'form-control',  # Classe Bootstrap (optionnelle)
            'style': 'width: 62%; padding: 8px; border-radius: 5px; border: none; height: 40px',
    })
    )

    dat_recep = forms.DateField(
        label="Date de réception",
        required=False,
        widget=forms.TextInput(attrs={'size': '10', 'placeholder': 'YYYY‑MM‑DD', 'class': 'form-control'}),
        input_formats=['%Y-%m-%d'],
    )

    saisi = forms.CharField(
        label="Responsable de saisie",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'size': '50', 'class': 'form-control'}),
    )

    dat_saisi = forms.DateField(
        label="Date de saisie",
        required=False,
        widget=forms.TextInput(attrs={'size': '10', 'placeholder': 'YYYY‑MM‑DD', 'class': 'form-control'}),
        input_formats=['%Y-%m-%d'],
    )

    dat_envoi = forms.DateField(
        label="Date d'envoi au traitement",
        required=False,
        widget=forms.TextInput(attrs={'size': '10', 'placeholder': 'YYYY‑MM‑DD', 'class': 'form-control'}),
        input_formats=['%Y-%m-%d'],
    )



