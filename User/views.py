from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import Reservations
from Administrator.models import Salles

def reserver(request):
    #Les salles disponibles
    salles_disponibles=Salles.objects.filter(reservations__isnull=True)

    if request.method=='POST':
        #Les données du formulaire
        salle_id=request.POST.get('salle_id')
        date=request.POST.get('date')
        heure=request.POST.get('heure')
        equipment_ids=request.POST.getlist('equipment')
        nbr_invt=int(request.POST.get('nbr_invt', 0))

        if nbr_invt<0 or nbr_invt>50:
            return render(request,'User/reserver.html',{'error_message':'Le nombre d\'invités dépassent la capacité...'})

        #Création d'une nouvelle réservation
        reservation=Reservations.objects.create(
            salle_id=salle_id,
            date=date,
            heure=heure,
            nbr_invt=nbr_invt
        )

        #Ajouter les équipements
        reservation.equipment.set(equipment_ids)
        #Rediriger vers la page de confirmation avec l'ID de la réservation
        return redirect('confirmation',reservation_id=reservation.id)

    #Revenir à la page de réservation avec les salles disponibles
    return render(request,'User/reserver.html',{'salles_disponibles':salles_disponibles})

# la liste de reservations 
def home(request):
      context = {
        'listReservations': Reservations.objects.all()
        }

class reservationsListView(ListView):
     model=Reservations
     template_name='User/ListesReservations.html'
     context_object_name='listReservations'
