"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=200)
    periodo = models.CharField(max_length=50)
    instituicao = models.CharField(max_length=200)
class Vestibular(models.Model):
    nome = models.CharField(max_length=200)
class Inscricoes(models.Model):
    id = models.CharField()
    nome = models.CharField(max_length=50)

