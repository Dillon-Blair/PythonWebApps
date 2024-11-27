from django.db import models

# Create your models here.

#From Mark Seaman
class Superhero(models.Model):
    heroid = models.TextField()
    name = models.CharField(max_length=200)
    strengths = models.TextField()
    weaknesses = models.TextField()


