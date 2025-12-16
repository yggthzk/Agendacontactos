from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Contacto

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User#serializador para el modelo
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'