from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    # Ajoutez d'autres champs selon vos besoins


USER_LEVEL_CHOICES = [
    ('Utilisateur', 'Utilisateur'),
    ('Modérateur', 'Modérateur'),
    ('Administrateur', 'Administrateur'),
    # Ajoutez d'autres choix de niveaux si nécessaire
]

class CustomUser(AbstractUser):
    # Vos autres champs personnalisés si nécessaire
    
    user_level = models.CharField(max_length=50, choices=USER_LEVEL_CHOICES, default='Utilisateur')
    
    # Spécifiez des related_names différents pour éviter les conflits
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        related_name='custom_user_permissions',  # Nouveau related_name
        blank=True,
        help_text='Specific permissions for this user.'
    )
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        related_name='custom_user_groups',  # Nouveau related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'
    )

class Article(models.Model):
    TYPE_CHOICES = (
        ('blog', 'Blog'),
        ('actualite', 'Actualité'),
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    # Ajoutez d'autres champs nécessaires pour votre modèle
