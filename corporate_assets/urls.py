from django.urls import path
from rest_framework import routers
from corporate_assets.views import (
    CompanyViewSet,
    EmployeeViewSet,
    AssetViewSet,
    AssetLogViewSet
)

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet, basename="company")
router.register(r'employee', EmployeeViewSet, basename="employee")
router.register(r'asset', AssetViewSet, basename="assets")
router.register(r'asset-log', AssetLogViewSet, basename="assets_logs")

urlpatterns = [
    
]+router.urls
