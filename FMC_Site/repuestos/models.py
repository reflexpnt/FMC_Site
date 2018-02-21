from django.db import models
from django import forms

class Articulo(models.Model):
            partNum = models.CharField(max_length=10)
            description = models.CharField(max_length=200, blank=True, null=True)


            def __str__(self):
                return self.partNum