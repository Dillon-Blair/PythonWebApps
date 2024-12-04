from django.db import models
from django.contrib.auth.models import User

#class Reporter(models.Model):
    #name = models.CharField(max_length=100)
    #email = models.EmailField()
    #user = models.OneToOneField(User, on_delete=models.CASCADE)


class Hero(models.Model):
    heropk = models.AutoField(primary_key=True) #hero ph
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, null =True, editable=False) #Causing problems

    SuperheroName = models.CharField(max_length=200) #title.
    name = models.CharField(max_length=200) # real identity

    strengths = models.CharField(max_length=200) # Their strengths
    weaknesses = models.CharField(max_length=200) # Their weaknesses

    age = models.CharField(max_length=200)  # Their age
    residence = models.CharField(max_length=200) # Where they live

    food = models.CharField(max_length=200) # weakness 2

    image = models.CharField(max_length=200) # imagelocation

    def __str__(self):
        return f"{self.heropk}. {self.SuperheroName} - {self.name}"