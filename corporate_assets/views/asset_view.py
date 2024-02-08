from rest_framework.viewsets import ModelViewSet
from corporate_assets.serializers import AssetSerializer, AssetLogSerializer
from corporate_assets.models import Asset, AssetLog


class AssetViewSet(ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


class AssetLogViewSet(ModelViewSet):
    queryset = AssetLog.objects.all()
    serializer_class = AssetLogSerializer