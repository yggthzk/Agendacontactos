from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactoViewSet, RegisterView, DashboardView

router = DefaultRouter()
router.register(r'contactos', ContactoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('dashboard/', DashboardView.as_view(), name='dashboard_stats'),
]#integrando dashboard de estadisticas