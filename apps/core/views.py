from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def frontpage(request):
    return render(request, "core/frontpage.html")


def signup(request):
    if request.method == "POST":
        # On récupère le formulaire issu de la requête de création de compte
        form = UserCreationForm(request.POST)

        # Si le formulaire est valide
        if form.is_valid():
            # On essaye de créer l'utilisateur
            user = form.save()
            login(request, user)

            # Si c'est bon, on redirige vers frontpage
            return redirect("frontpage")
    else:
        # On crée un formulaire vide
        form = UserCreationForm()

    return render(request, "core/signup.html", {"form": form})
