import datetime

from django.db import models


# Create your models here.

# Models Adherent regroupe les information nécessaire pour un adhérent
class Adherent(models.Model):
    Prenom = models.CharField(max_length=50)
    Nom = models.CharField(max_length=50)
    Adresse_Rue = models.CharField(max_length=50)
    Adresse_CP = models.CharField(max_length=50)
    Adresse_Ville = models.CharField(max_length=50)
    Telephone = models.CharField(blank=False, max_length=10)
    Mail = models.CharField(max_length=50)
    Genre = models.CharField(max_length=50)
    Niveau = models.CharField(max_length=20)
    Numero_Licence = models.CharField(max_length=20)
    Date_Naissance = models.DateTimeField()
    Certificat_Medical = models.CharField(max_length=50)
    Date_Certificat = models.DateTimeField()
    Pointure = models.CharField(max_length=50)
    Taille = models.CharField(max_length=50)
    Date_inscription = models.DateTimeField()

    def __str__(self):
        return self.Nom + self.Prenom


# Models Entraineur  hérite de Adhérent, un entraineur est forcément un adhérent

class Entraineur(models.Model):
    adherent = models.OneToOneField(
        Adherent, on_delete=models.CASCADE, related_name="entraineur", primary_key=True,
    )

    def __str__(self):
        return self.adherent.Nom + self.adherent.Prenom


# Models Coach  hérite de Entraineur, un coach est forcément un entraineur

class Coach(models.Model):
    entraineur = models.OneToOneField(
        Entraineur, on_delete=models.CASCADE, primary_key=True,
    )

    def __str__(self):
        return self.entraineur.adherent.Nom + self.entraineur.adherent.Prenom


# Models Entrainement regroupe les information nécessaire pour un entrainement

class Entrainement(models.Model):
    Dates = models.DateTimeField()
    Lien_fichier = models.CharField(max_length=300)
    entraineurs = models.ManyToManyField(Entraineur)
    coach = models.ForeignKey(Coach, related_name="coachs_entrainement", on_delete=models.CASCADE)

    # Models Role, contient les différent role occupé par des adhérent dans l'association, différent des groupes


class Role(models.Model):
    Nom = models.CharField(max_length=50)
    adherents = models.ManyToManyField(Adherent)

    def __str__(self):
        return self.Nom
