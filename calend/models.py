from django.db import models
from django.contrib.auth.models import User
 
class Reserve(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
 
    class Meta:  
        db_table = "tblevents"



class Salle(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    capacite = models.IntegerField()
    equipements = models.TextField(blank=True)

class Reservation(models.Model):
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    objet = models.CharField(max_length=150)
    description = models.TextField(blank=True)

class Utilisateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
