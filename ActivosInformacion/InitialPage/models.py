from django.db import models
from Users.models import User

# Create your models here.
class TypesActives(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(max_length=200)

class SubtypesActives(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(max_length=200)
    typeActive = models.ForeignKey(TypesActives, on_delete=models.CASCADE, null=True)

class Actives(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(max_length=200)
    quantity = models.IntegerField()
    typeActive = models.ForeignKey(TypesActives, on_delete=models.CASCADE, null=True)

class ActivesDependecies(models.Model):
    typeActiveDependen = models.ForeignKey(TypesActives, on_delete=models.CASCADE, null=True, related_name="DependentTypeActive")
    subactiveDependent = models.ForeignKey(SubtypesActives, on_delete=models.CASCADE, null=True, related_name="DependentSubtypeActive")
    typeActiveIndependent = models.ForeignKey(TypesActives, on_delete=models.CASCADE, null=True, related_name="IndependentTypeActive")
    subactiveIndependent = models.ForeignKey(SubtypesActives, on_delete=models.CASCADE, null=True, related_name="IndependentSubtypeActive")
    