from django.shortcuts import render
from contactos.models import Visita

def home(request):
    obj, created = Visita.objects.get_or_create(id=1)
    obj.conteo += 1
    obj.save()
    return render(request, "index.html")

#vista por defecto (Login y main)
#logica conteo de Visitas de la pagina