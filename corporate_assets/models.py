from django.db import models
from django.contrib.auth.models import User
from core.models import BaseModel
# Create your models here.


class Company(BaseModel):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    contact_email = models.EmailField(max_length=150, unique=True)
    contact_number = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ("-created_at",)


class Employee(BaseModel):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="company_employee"
    )
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=150, unique=True)
    phone = models.CharField(max_length=15)
    position = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f"{self.company.name}-{self.name}"
    
    class Meta:
        ordering = ("-created_at",)


class Asset(BaseModel):
    asset_type = models.CharField(max_length=100)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="company_asset"
    )
    description = models.CharField(max_length=350, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.company.name} - {self.asset_type}"
    
    class Meta:
        ordering = ("-created_at",)


class AssetLog(BaseModel):
    asset = models.ForeignKey(
        Asset, on_delete=models.CASCADE, related_name="asset_log"
    )
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="employee_log"
    )
    check_out_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    check_out_condition = models.CharField(max_length=100)
    return_condition = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.asset.asset_type}-{self.employee.name}-{self.check_out_date}"
    
    class Meta:
        ordering = ("-created_at",)