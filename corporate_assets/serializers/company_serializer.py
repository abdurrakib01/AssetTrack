from rest_framework import serializers
from corporate_assets.models import Company
from django.contrib.auth.models import User


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class CompanyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("name", "address", "contact_email", "contact_number")