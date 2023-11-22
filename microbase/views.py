from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import RechercheForm
from django.views.generic import ListView
from django.contrib.auth import  authenticate, login
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView



def index(request):
    # Votre logique pour récupérer les données ou effectuer d'autres opérations pour la page d'index
    return render(request, 'index.html')

def recherche(request):
    
    context = {
        'titre': 'Résultats de la recherche',
        # Autres données à passer au template
    }
    return render(request, 'recherche.html', context)


def recherche(request):
    if request.method == 'POST':
        form = RechercheForm(request.POST)
        if form.is_valid():
            terme_recherche = form.cleaned_data['terme_recherche']
            # Logique de recherche basée sur terme_recherche
            # Récupération des résultats en fonction du terme de recherche
            # Puis passez ces résultats au contexte
            context = {
                'titre': 'Résultats de la recherche pour : ' + terme_recherche,
                # Autres données à passer au template
            }
            return render(request, 'recherche.html', context)
    else:
        form = RechercheForm()

    context = {
        'titre': 'Recherche',
        'form': form,
    }
    return render(request, 'recherche.html', context)


class BlogListView(ListView):
    model = Article
    template_name = 'blog_list.html'  # Nom du template pour afficher la liste des articles de blog
    context_object_name = 'articles'  # Nom du contexte pour les articles de blog
    queryset = Article.objects.filter(type='blog')  # Filtrer les articles de type 'blog'

class ActualiteListView(ListView):
    model = Article
    template_name = 'actualite_list.html'  # Nom du template pour afficher la liste des actualités
    context_object_name = 'actualites'  # Nom du contexte pour les actualités
    queryset = Article.objects.filter(type='actualite')  # Filtrer les articles de type 'actualite'


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Rediriger vers la page après la connexion (remplacez 'index' par votre vue)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def profile(request):
    # Logique de la vue de profil
    return render(request, 'profile.html')  # Remplacez 'profile.html' par votre modèle de profil