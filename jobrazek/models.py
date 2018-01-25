from django.db import models

# Create your models here.

class Jobrazek(models.Model):
    obrazkowa_sciezka = models.ImageField(upload_to='foteczki/')
