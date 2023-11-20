from django.db import models

# Create your models here.

class Persona(models.Model):
    name = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=200, null=False, primary_key=True)
    address = models.CharField(max_length=200, null=False)
    phone = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name

