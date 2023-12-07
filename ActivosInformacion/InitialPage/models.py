from django.db import models
from Users.models import Users

# Create your models here.
class Workload(models.Model):
    name = models.CharField(max_length=50, null=False)

class TypeAssets(models.Model):
    name = models.CharField(max_length=50, null=False)

class SubtypeAssets(models.Model):
    name = models.CharField(max_length=50, null=False)
    type = models.ForeignKey(TypeAssets, null=True, on_delete=models.CASCADE)

class Departments(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(max_length=200, null=False)
    workload = models.ManyToOneRel(Workload, on_delete=models.CASCADE, to=Workload, field_name="workload")

class Assets(models.Model):
    code = models.CharField(max_length=5)
    origin = models.CharField(max_length=20)
    name = models.TextField(max_length=20)
    ubicationTipe = models.CharField(max_length=20)
    ubication = models.CharField(max_length=20)
    quantity = models.IntegerField()
    Characteristic = models.TextField(max_length=50)
    tipe = models.ForeignKey(TypeAssets, on_delete=models.CASCADE)
    responsableArea = models.ForeignKey(Departments, null=False, on_delete=models.CASCADE)
    responsableUser = models.ForeignKey(Users, null=False, on_delete=models.CASCADE)
    