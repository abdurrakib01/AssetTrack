from rest_framework import serializers
from corporate_assets.models import Employee, Company
from corporate_assets.serializers import CompanyDetailsSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['company'] = CompanyDetailsSerializer(instance.company).data
        return representation
