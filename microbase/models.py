from django.db import models

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    # Ajoutez d'autres champs selon vos besoins


from django.db import models

class Article(models.Model):
    TYPE_CHOICES = (
        ('blog', 'Blog'),
        ('actualite', 'Actualité'),
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    # Ajoutez d'autres champs nécessaires pour votre modèle
