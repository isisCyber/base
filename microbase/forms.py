from django import forms

class RechercheForm(forms.Form):
    terme_recherche = forms.CharField(label='Terme de recherche', max_length=100)
    # Ajoutez d'autres champs pour votre formulaire si nécessaire
