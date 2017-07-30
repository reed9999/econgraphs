from django.db import models

# Create your models here.

class GraphableFunction (models.Model):
    name = models.CharField(max_length=200)
    function_spec = models.CharField(max_length=200)

class Source (models.Model):
    graphable_functions = models.ManyToManyField(GraphableFunction)
    authors = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    #zotero_id = models.IntegerField()
    zotero_key = models.CharField(max_length=8)

    def __str__(self):
        return "%s: %s (Z: %s)" % (self.authors, self.title, self.zotero_key)