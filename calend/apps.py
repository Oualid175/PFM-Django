from django.apps import AppConfig

class CalendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'calend'

class ReservationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reservation'
