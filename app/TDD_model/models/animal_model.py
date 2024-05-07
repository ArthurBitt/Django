from django.db import models

# Create your models here.
class Animal(models.Model):
    name_animal = models.CharField(max_length=100)
    predador = models.CharField(max_length=100)
    venenoso = models.CharField(max_length=100)
    domestico = models.CharField(max_length=100)

    def __str__(self):
        return self.name_animal