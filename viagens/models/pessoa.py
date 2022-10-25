from unittest.util import _MAX_LENGTH
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    