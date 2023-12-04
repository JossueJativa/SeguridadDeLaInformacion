from django.db import models
from InitialPage.models import TypesActives, SubtypesActives
from Users.models import User

# Create your models here.
class ResponsableUnity(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField(max_length=100)

class Origin(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField(max_length=100)

class CompanyAssets(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField(max_length=100)
    ubication = models.TextField(max_length=100)
    quantity = models.IntegerField()
    notes = models.TextField()
    typeofasset = models.CharField(max_length=10)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)

class CompanyAssetsTypes(models.Model):
    companyassets = models.ForeignKey(CompanyAssets, on_delete=models.CASCADE)
    type = models.ForeignKey(TypesActives, on_delete=models.CASCADE)
    subtype = models.ForeignKey(SubtypesActives, on_delete=models.CASCADE, null=True)

class CompanyAssetsUnityResponsable(models.Model):
    companyassets = models.ForeignKey(CompanyAssets, on_delete=models.CASCADE)
    responsableunity = models.ForeignKey(ResponsableUnity, on_delete=models.CASCADE)

class CompanyAssetsUser(models.Model):
    companyassets = models.ForeignKey(CompanyAssets, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ActivesDependecies(models.Model):
    dependencypercentage = models.FloatField()
    descriptiondependency = models.TextField(max_length=100)
    Interviewed = models.ForeignKey(User, on_delete=models.CASCADE)
    companyassetsindependent = models.ForeignKey(CompanyAssets, on_delete=models.CASCADE, related_name='companyassetsindependent')
    companyassetsdependent = models.ForeignKey(CompanyAssets, on_delete=models.CASCADE, related_name='companyassetsdependent')