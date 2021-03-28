from django.db import models

class Categories(models.Model):
    index = models.IntegerField()
    category = models.CharField(max_length=100)

class Level(models.Model):
    level = models.CharField(max_length=100)
