from django.contrib import admin
from .models import Salle,Reservation,Utilisateur

admin.site.register(Salle)
admin.site.register(Reservation)
admin.site.register(Utilisateur)
