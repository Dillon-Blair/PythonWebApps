from django.db import models

# Create your models here.

class Superhero(models.Model):
    heroid = models.TextField()
    name = models.CharField(max_length=200)
    strengths = models.TextField()
    weaknesses = models.TextField()


# python3 manage.py shell
# from hero.models import Superhero

# Superhero.objects.create(name='Black Widow', description='Natalia Romanova', image='None')

# w = Superhero.objects.get(name='Black Widow')
# print(w.description)

#for s in Superhero.objects.filter(name='Black Widow'):
#    print(w.description, w.name)

#w = Superhero.objects.get(name='Black Widow')
#w.description='Natasha Romanoff'
#w.save()

#Superhero.objects.get(name='Black Widow').delete()
