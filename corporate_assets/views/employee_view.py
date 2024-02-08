from rest_framework.viewsets import ModelViewSet
from corporate_assets.serializers import EmployeeSerializer
from corporate_assets.models import Employee


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

