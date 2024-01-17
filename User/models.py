from django.db import models

class Reservations(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    salle_id = models.ForeignKey('Administrator.Salles', on_delete=models.CASCADE, related_name='salles')
    date = models.DateField()
    heure = models.TimeField()
    equipment = models.ManyToManyField('Administrator.Salles', related_name='reservations_set')
    nbr_invt = models.IntegerField()
    def __str__(self) -> str:
        return super().__str__()
