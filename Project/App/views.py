from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse

def accueil(request):
    context = {
        'titre_section': 'Documentation du HCP',
        'message_bienvenue': 'Bienvenue sur la page dédiée au Centre National de Documentation.',
    }
    return render(request, 'accueil.html', context)

#def collecte(request):
#    context = {
#        'titre_section': 'Collecte de données',
#        'message_bienvenue': 'Bienvenue sur la page de collecte de données.',
#    }
#    return render(request, 'collecte.html', context)

def gestion(request):
    context = {
        'titre_section': 'Gestion des données',
        'message_bienvenue': 'Bienvenue sur la page de gestion des données.',
    }
    return render(request, 'gestion.html', context)

def bilan(request):
    context = {
        'titre_section': 'Bilan des activités',
        'message_bienvenue': 'Bienvenue sur la page de bilan des activités.',
    }
    return render(request, 'bilan.html', context)

def rendement(request):
    context = {
        'titre_section': 'Rendement des activités',
        'message_bienvenue': 'Bienvenue sur la page de rendement des activités.',
    }
    return render(request, 'rendement.html', context)

def statistiques(request):
    context = {
        'titre_section': 'Statistiques',
        'message_bienvenue': 'Bienvenue sur la page des statistiques.',
    }
    return render(request, 'statistiques.html', context)

def recherche(request):
    context = {
        'titre_section': 'Recherche',
        'message_bienvenue': 'Bienvenue sur la page de recherche.',
    }
    return render(request, 'recherche.html', context)

from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from .Forms import PeriodiqueForm, MonographieForm, IndexeurForm, IndexationControleForm, PriseDeVueForm

def collecte_view(request):
    form_type = request.GET.get('form_type', None)
    form = None

    forms_classes = {
        'periodique': PeriodiqueForm,
        'monographie': MonographieForm,
        'indexeur': IndexeurForm,
        'indexation et contrôle': IndexationControleForm,
        'prise de vue': PriseDeVueForm,
    }

    if form_type in forms_classes:
        form_class = forms_classes[form_type]

        if request.method == 'POST':
            forms = form_class(request.POST)
            if forms.is_valid():
                username = forms.cleaned_data['username']
                password = forms.cleaned_data['password']

                destinations = {
                    'periodique': 'collecte',
                    'monographie': 'collecte',
                    'indexeur': 'suivi',
                    'indexation et contrôle': 'indexation',
                    'prise de vue': 'vue',
                }
                required_destination = destinations[form_type]

                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT COUNT(*) FROM admin WHERE login = %s AND pass = %s AND destination = %s",
                        [username, password, required_destination]
                    )
                    count = cursor.fetchone()[0]

                if count > 0:
                    # Redirection vers la page appropriée avec reverse
                    redirect_names = {
                        'periodique': 'periodique',           # nom de la vue dans urls.py
                        'monographie': 'monographie',
                        'indexeur': 'indexeur',
                        'indexation et contrôle': 'indexation_control',
                        'prise de vue': 'prise_vue',
                    }
                    # Optionnel : tu peux aussi mettre à jour la session ici si besoin
                    request.session['authenticated'] = True
                    return redirect(reverse(redirect_names[form_type]))
                else:
                    messages.error(request, "Veuillez bien saisir vos identifiants pour le module:  " + form_type.upper())
        else:
            form = form_class()
    else:
        form = None

    return render(request, 'collecte.html', {'form': form, 'form_type': form_type})

def periodique_view(request):
    if not request.session.get('authenticated', False):
        return redirect('collecte')
    return render(request, 'Collecte/periodique.html')

def monographie_view(request):
    if not request.session.get('authenticated', False):
        return redirect('collecte')
    return render(request, 'Collecte/monographie.html')

def indexeur_view(request):
    if not request.session.get('authenticated', False):
        return redirect('collecte')
    return render(request, 'Collecte/indexeur.html')

def indexation_control_view(request):
    if not request.session.get('authenticated', False):
        return redirect('collecte')
    return render(request, 'Collecte/indexation_control.html')

def prise_vue_view(request):
    if not request.session.get('authenticated', False):
        return redirect('collecte')
    return render(request, 'Collecte/priseVue.html')


from .Forms import SearchFormPeriodique

from .Forms import SearchFormPeriodique

# def periodique_view(request):
#     if not request.session.get('authenticated', False):
#         return redirect('collecte')

#     form = SearchFormPeriodique(request.GET or None, prefix='search')
#     query = form.cleaned_data['query'] if form.is_valid() else ''

#     return render(request, 'Collecte/periodique.html', {
#         'form': form,
#         'query': query,
#     })


# from django.shortcuts import render, redirect
# from django.db import transaction
# from .forms import PeriodiqueForm
# from .models import Doc, Ecriture, Edition, Fournit, Collecte

# def ajouter_periodique(request):
#     # On garde "form" comme variable pour éviter conflit. On utilise "form_obj"
#     if request.method == "POST":
#         form_obj = PeriodiqueForm(request.POST)
#         if form_obj.is_valid():
#             data = form_obj.cleaned_data
#             try:
#                 with transaction.atomic():
#                     # 1️⃣ Création de l'objet Doc
#                     doc = Doc.objects.create(
#                         n_enregistrement = int(data['isbn']) if data['isbn'] else None,
#                         titre = data['titre'],
#                         titre_article = data.get('stitre', ''),
#                         pages = data.get('pages', ''),
#                         domaine = data['critere'],
#                         type = data['type'],
#                         periodicite = '0',
#                         vol = data.get('vol', ''),
#                         tom = data.get('tom', ''),
#                         num = data.get('num', ''),
#                         statut = '0',
#                         n_periodique = None,
#                         lang = data['lang']
#                     )
#                     n_enc = doc.n_enregistrement

#                     # 2️⃣ Auteur → Ecriture
#                     if data.get('auteur'):
#                         Ecriture.objects.create(
#                             auteur = data['auteur'],
#                             n_enregistrement = n_enc
#                         )

#                     # 3️⃣ Edition
#                     if data.get('dat_edit'):
#                         Edition.objects.create(
#                             editeur = data['titre'],  # ou autre champ si diffère
#                             n_enregistrement = n_enc,
#                             date_edition = data['dat_edit'],
#                             ville_edition = ''
#                         )

#                     # 4️⃣ Fournit (source + date réception)
#                     if data.get('src'):
#                         Fournit.objects.create(
#                             source = data['src'],
#                             n_enregistrement = n_enc,
#                             date_reception = data.get('dat_recep'),
#                             obligation = ''
#                         )

#                     # 5️⃣ Collecte (responsable de saisie)
#                     if data.get('saisi'):
#                         Collecte.objects.create(
#                             nomrc = data['saisi'],
#                             n_enregistrement = n_enc,
#                             datsaisi_c = data.get('dat_saisi')
#                         )

#                 return redirect('ajout_success')  # À adapter
#             except Exception as e:
#                 form_obj.add_error(None, f"Erreur base de données : {e}")
#     else:
#         form_obj = PeriodiqueForm()
#     return render(request, 'accueil', {'form': form_obj})

# views.py

from django.shortcuts import render, redirect
from django.db import transaction
from .Forms import SearchFormPeriodique, PeriodiqueFormGeneral
from .models import Doc, Ecriture, Edition, Fournit, Collecte

def periodique_view(request):
    if not request.session.get('authenticated', False):
        return redirect('collecte')

    # Formulaires avec préfixes
    form_search = SearchFormPeriodique(request.GET or None, prefix='search')
    form_period = PeriodiqueFormGeneral(request.POST or None, prefix='period')

    # Traitement du GET (recherche)
    if request.method == 'GET' and 'submit_search' in request.GET and form_search.is_valid():
        query = form_search.cleaned_data['query']
    else:
        query = ''

    # Traitement du POST (ajout périodique)
    if request.method == 'POST' and 'submit_period' in request.POST:
        if form_period.is_valid():
            data = form_period.cleaned_data
            try:
                with transaction.atomic():
                    # Créations des objets comme avant
                    doc = Doc.objects.create(
                        n_enregistrement=int(data['isbn']) if data['isbn'] else None,
                        titre=data['titre'],
                        titre_article=data.get('stitre', ''),
                        pages=data.get('pages', ''),
                        domaine=data['critere'],
                        type='p',
                        periodicite=data['radio1'],
                        vol=data.get('vol', ''),
                        tom=data.get('tom', ''),
                        num=data.get('num', ''),
                        statut='0',
                        n_periodique=None,
                        lang=data['lang']
                    )
                    n_enc = doc.n_enregistrement

                    if data.get('auteur'):
                        Ecriture.objects.create(auteur=data['auteur'], n_enregistrement=n_enc)
                    if data.get('dat_edit'):
                        Edition.objects.create(
                            editeur=data['titre'], n_enregistrement=n_enc,
                            date_edition=data['dat_edit'], ville_edition=''
                        )
                    if data.get('src'):
                        Fournit.objects.create(
                            source=data['src'], n_enregistrement=n_enc,
                            date_reception=data.get('dat_recep'), obligation=''
                        )
                    if data.get('saisi'):
                        Collecte.objects.create(
                            nomrc=data['saisi'], n_enregistrement=n_enc,
                            datsaisi_c=data.get('dat_saisi')
                        )
                return redirect('ajout_success')
            except Exception as e:
                form_period.add_error(None, f"Erreur base de données : {e}")
    return render(request, 'Collecte/periodique.html', {
        'form_search': form_search,
        'form_period': form_period,
        'query': query,
        'champs1': ['stitre', 'titre', 'auteur'],
        'champs2': ['vol', 'tom', 'num'],
        'champs3': ['dat_edit', 'pages'],
        'champs4':['critere', 'lang', 'src', 'type'],
        'champs5': ['dat_recep', 'saisi', 'dat_saisi'],
        'champs6': ['dat_envoi']
    })
