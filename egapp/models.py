from django.db import models

# Create your models here.

class FunctionsToGraph (models.Model):
    name = models.CharField(max_length=200)
    function_spec = models.CharField(max_length=200)

class Sources (models.Model):
    functions_to_graph = models.ManyToManyField(FunctionsToGraph)
    authors = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    zotero_id = models.IntegerField()