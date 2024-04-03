from django.db import models

# Create your models here.
class Batiment(models.Model):
    name = models.CharField(max_length=255)
    surface = models.FloatField(null=True, blank=True, default=None)
    usage = models.IntegerField(null=True, blank=True, default=None)
    periode_de_reference = models.IntegerField()

class Zone(models.Model):
    name = models.CharField(max_length=255)
    surface = models.FloatField()
    usage = models.IntegerField()
    bat_id = models.ForeignKey("Batiment", on_delete=models.CASCADE)
    
    # construction_elements = models.XField()
