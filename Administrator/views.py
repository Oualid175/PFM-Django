from django.views.generic import ListView
from django.shortcuts import render,redirect,get_object_or_404
from .models import Equipment,Salles
from User.models import Reservations

def home(request):
    context = {
        'listSalle': Salles.objects.all()
    }
    
def Confirmer(request,reservation_id):
    reservation=get_object_or_404(Reservations,id=reservation_id)
    salle=get_object_or_404(salle,id=reservation.salle_id)
    if salle.is_reserved:
        return redirect('erreur',message='La salle est déjà réservée.')

    reservation.confirmed=True
    reservation.save()

    salle.is_reserved=True
    salle.save()

    equipment=Equipment.objects.filter(reservations=reservation)

    return render(request,'Administrator/confirmer.html',{'reservation':reservation,'salle': salle,'equipment':equipment})

class SalleListView(ListView):
    model=Salles
    template_name='Administrator/index.html'
    context_object_name='listSalle'
