from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    cpf = models.CharField(max_length=11, blank=True, null=True, unique=True)
    telefone = models.CharField(max_length=11, blank=True, null=True, unique=True)
    data_nascimento = models.DateField(blank=True, null=True)
