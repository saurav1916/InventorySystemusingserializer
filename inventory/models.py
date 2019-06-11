from django.db import models

# Create your models here.
class inven(models.Model):
    name=models.CharField(max_length=10)
    quantity=models.CharField(max_length=10)