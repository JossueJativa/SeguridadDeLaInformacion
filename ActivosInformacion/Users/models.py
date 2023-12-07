from django.db import models
from django.contrib.auth.models import AbstractUser
from InitialPage.models import Departments, Workload

# Create your models here.
class Users(AbstractUser):
    celular = models.CharField(max_length=10, null=False)
    department = models.ForeignKey(Departments, null=False)
    workload = models.ForeignKey(Workload, null=False)