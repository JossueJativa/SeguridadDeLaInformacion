from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Workload(models.Model):
    name = models.CharField(max_length=50, null=False)

class User(AbstractUser):
    celular = models.CharField(max_length=10, null=False)
    workload = models.ForeignKey(Workload, on_delete=models.CASCADE, null=True)