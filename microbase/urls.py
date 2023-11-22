from django.urls import path
from . import views
from .views import BlogListView, ActualiteListView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.login_view,name = 'login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('profil/', views.profile, name='profile'),
    path('recherches/', views.recherche, name='recherche'),
    path('blog/',BlogListView.as_view(), name='blog'),
    path('actualites/',ActualiteListView.as_view(), name='actu'),
    # Ajoutez d'autres chemins d'accès si nécessaire pour votre application
]
