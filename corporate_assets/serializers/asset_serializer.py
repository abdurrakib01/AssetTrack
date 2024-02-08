from rest_framework import serializers
from corporate_assets.models import Asset, AssetLog, Employee
from corporate_assets.serializers import CompanyDetailsSerializer


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['company'] = CompanyDetailsSerializer(instance.company).data
        return representation


class AssetDetailSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source="company.name")

    class Meta:
        model = Asset
        fields = ("asset_type", "description", "company")


class EmployeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("name", "email", "phone", "position")


class AssetLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetLog
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['asset'] = AssetDetailSerializer(instance.asset).data
        representation['employee'] = EmployeeDetailSerializer(
            instance.employee.all(), many=True
        ).data
        return representation
