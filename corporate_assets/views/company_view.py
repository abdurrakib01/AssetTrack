from rest_framework.viewsets import ModelViewSet
from corporate_assets.serializers import CompanySerializer
from corporate_assets.models import Company


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

