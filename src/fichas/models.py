from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Usuario(models.Model):
    nome = models.TextField()