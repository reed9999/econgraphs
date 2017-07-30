from django.db import models

# Create your models here.

class GraphableFunction (models.Model):
    name = models.CharField(max_length=200)
    function_spec = models.CharField(max_length=200)

class Source (models.Model):
    graphable_functions = models.ManyToManyField(GraphableFunction)
    authors = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    zotero_id = models.IntegerField()