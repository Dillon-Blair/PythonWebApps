from django.db import models

class Hero(models.Model):
    heropk = models.AutoField(primary_key=True)

    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    strength = models.CharField(max_length=200)
    weakness = models.CharField(max_length=200)

    age = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    food = models.CharField(max_length=200)
    music = models.CharField(max_length=200)

    image = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.heropk}. {self.title} - {self.name}"