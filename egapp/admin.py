from django.contrib import admin

# Register your models here.
from .models import GraphableFunction, Source
admin.site.register(GraphableFunction)
admin.site.register(Source)