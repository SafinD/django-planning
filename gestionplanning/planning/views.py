from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
# authentication/views.py
from django.views.generic import TemplateView
from .models import Adherent
from django.shortcuts import redirect, render
from django.views import generic

from . import forms


# Procédure de logout qui permet de déconnecter un utilisateur du site et redirige vers la page login
def logout_user(request):
    logout(request)
    return redirect('login')


# Views Login, permet la connexion d'un utilisateur a condition qu'il ai été créé.
def login_page(request):
    form = forms.LoginForm()
    message = ''
    adherents = Adherent.objects.all()
    # Lorsque l'utilsateur clique sur ce connecter les donné vont être envoyer
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)  # On récupère les donnée du formulaire
        # On valide les données du formulaire avec le is_valid()
        if form.is_valid():
            # authneticate() permet de vérifier si l'username et password existe bien.
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            # Si l'username et le password sont bon on passe a la connexion
            if user is not None:
                # La fonction Login() gère la connexion
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'planning/login.html', context={'form': form, 'message': message, 'adherents': adherents})


def index(request):
    adherents = Adherent.objects.all()
    return render(request, 'planning/index.html', {'adherents': adherents})
