from django.db import models
# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    object = models.Manager()
    DoesNotExist = models.Manager

class Company(models.Model):
    name = models.CharField(max_length=30)

class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()

