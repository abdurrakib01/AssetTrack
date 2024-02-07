from rest_framework import serializers
from django.contrib.auth.models import User

    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(
        style={'input_type': 'password'},
        required=True
    )