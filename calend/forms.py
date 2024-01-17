from .models import Reservation
from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime

class ReservationForm(forms.ModelForm):
    class Meta:
        model=Reservation
        fields=['salle','utilisateur','date_debut','date_fin','objet','description']
        widgets = {
            'date_debut': AdminSplitDateTime(attrs={'class': 'form-control'}),
            'date_fin': AdminSplitDateTime(attrs={'class': 'form-control'}),
            'salle': forms.Select(attrs={'class': 'form-control'}),
            'utilisateur': forms.Select(attrs={'class': ' form-control '}),
            'objet': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
