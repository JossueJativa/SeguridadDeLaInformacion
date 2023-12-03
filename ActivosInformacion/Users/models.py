from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Status(models.Model):
    booleanStatus = models.BooleanField(null=True)

class TeamRoles(models.Model):
    name = models.CharField(max_length=20, null=True)
    role = models.CharField(max_length=20, null=True)
    responsability = models.TextField(max_length=100, null=True)
    competences = models.TextField(max_length=200, null=True)
    statusRole = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)

class User(AbstractUser):
    identity = models.CharField(max_length=13)
    teamRole = models.ForeignKey(TeamRoles, on_delete=models.CASCADE, null=True)
