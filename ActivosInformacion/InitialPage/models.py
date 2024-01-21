from django.db import models
from Users.models import User, Workload

# Create your models here.
class TypeAssets(models.Model):
    name = models.CharField(max_length=50, null=False)

class SubtypeAssets(models.Model):
    name = models.CharField(max_length=50, null=False)
    type = models.ForeignKey(TypeAssets, null=True, on_delete=models.CASCADE)

class Departments(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(max_length=200, null=False)
    workload = models.ForeignKey(Workload, on_delete=models.CASCADE, null=True)

class RiskType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

class Risk(models.Model):
    type = models.ForeignKey(RiskType, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    dimention = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class Assets(models.Model):
    code = models.CharField(max_length=5)
    name = models.TextField(max_length=20)
    ubicationType = models.CharField(max_length=20)
    ubication = models.CharField(max_length=20)
    quantity = models.IntegerField()
    characteristic = models.TextField(max_length=50)
    type = models.ForeignKey(TypeAssets, on_delete=models.CASCADE)
    responsableArea = models.ForeignKey(Departments, null=False, on_delete=models.CASCADE)
    responsableUser = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

class AssetsDependence(models.Model):
    percentaje = models.IntegerField()
    asset = models.ForeignKey(Assets, on_delete=models.CASCADE, related_name='assetIndepend')
    responsableUser = models.ForeignKey(User, on_delete=models.CASCADE)
    assetDepend = models.ForeignKey(Assets, on_delete=models.CASCADE, related_name='assetDepend')

class AssetsValue(models.Model):
    cuantityValue = models.IntegerField()
    cualityValue = models.CharField(max_length=15)
    description = models.CharField(max_length=15)
    dimentionValue = models.CharField(max_length=20)
    asset = models.ForeignKey(Assets, on_delete=models.CASCADE, null=True)

class AssetsRisk(models.Model):
    risktype = models.ForeignKey(RiskType, on_delete=models.CASCADE, null=True)
    risk = models.ManyToManyField(Risk)
    asset = models.ForeignKey(Assets, on_delete=models.CASCADE, null=True)
    dimention = models.CharField(max_length=255, null=True)

class SafeguardsTypes(models.Model):
    name = models.CharField(max_length=100)

class Safeguards(models.Model):
    type = models.ForeignKey(SafeguardsTypes, on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=15)
    name = models.CharField(max_length=100)

class SafeguardsRisk(models.Model):
    risk = models.ForeignKey(AssetsRisk, on_delete=models.CASCADE, null=True)
    safeguard = models.ManyToManyField(Safeguards)
