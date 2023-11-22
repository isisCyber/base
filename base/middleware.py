from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and not request.path_info == reverse('login'):
            return redirect('login')  # Rediriger vers la page de connexion si l'utilisateur n'est pas connecté
        return self.get_response(request)
