from django.urls import path
from . import views

urlpatterns = [
    path('accueil/', views.accueil, name='accueil'),
    path('collecte/', views.collecte_view, name='collecte'),
    path('gestion/', views.gestion, name='gestion'),
    path('bilan/', views.bilan, name='bilan'),
    path('rendement/', views.rendement, name='rendement'),
    path('statistiques/', views.statistiques, name='statistiques'),
    path('recherche/', views.recherche, name='recherche'),
    path('periodique/', views.periodique_view, name='periodique'),
    path('monographie/', views.monographie_view, name='monographie'),
    path('indexeur/', views.indexeur_view, name='indexeur'),
    path('indexation_control/', views.indexation_control_view, name='indexation_control'),
    path('prise-vue/', views.prise_vue_view, name='prise_vue'),
]
