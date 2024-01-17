from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Salles(models.Model):
    salle_id = models.AutoField(primary_key=True)
    capacite = models.IntegerField()
    equipment = models.ManyToManyField('Administrator.Equipment', related_name='salles_set')
    def __str__(self) -> str:
        return super().__str__()

    def equipment_names(self):
        return ', '.join(equip.name for equip in self.equipment.all())
