from django.contrib import admin
from .models import Contacto, Visita

admin.site.register(Contacto)
admin.site.register(Visita)
#Importando contactos y conteo devisitas de la pagina