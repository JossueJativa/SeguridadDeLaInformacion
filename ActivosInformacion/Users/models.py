from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=20)

class Responsabilities(models.Model):
    name = models.CharField(max_length=20)

class WorkPosition(models.Model):
    name = models.TextField(max_length=20)

class User(AbstractUser):
    identity = models.CharField(max_length=13)
    status = models.BooleanField(default=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    workPosition = models.ForeignKey(WorkPosition, on_delete=models.CASCADE, null=True)

class UserResponsabilities(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    responsability = models.ForeignKey(Responsabilities, on_delete=models.CASCADE, null=True)