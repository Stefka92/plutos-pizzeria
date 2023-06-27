from django.db import models

# Create your models here.
class item(models.model):
    name = models.CharField(max_lenght=50, null=False, blank=False)
    Date = models.BooLeanField(null=False, blank=False)