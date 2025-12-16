from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from .models import Contacto, Visita
from .serializers import ContactoSerializer, UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all().order_by('-fecha_creacion')
    serializer_class = ContactoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DashboardView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        total_contactos = Contacto.objects.count()
        
        try:
            visitas = Visita.objects.get(id=1).conteo
        except Visita.DoesNotExist:
            visitas = 0

        hace_una_semana = timezone.now() - timedelta(days=7)
        nuevos = Contacto.objects.filter(fecha_creacion__gte=hace_una_semana).count()
        antiguos = total_contactos - nuevos

        return Response({
            "total": total_contactos,
            "visitas": visitas,
            "nuevos": nuevos,
            "antiguos": antiguos
        })

def index_view(request):
    return render(request, 'index.html')