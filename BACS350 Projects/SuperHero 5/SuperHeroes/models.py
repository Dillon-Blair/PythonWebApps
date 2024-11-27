from django.db import models



#The same format as the Mark Seaman Lesson
class Hero(models.Model):
    heropk = models.AutoField(primary_key=True)

    SuperheroName = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    strengths = models.CharField(max_length=200)
    weaknesses = models.CharField(max_length=200)

    age = models.CharField(max_length=200)
    residence = models.CharField(max_length=200)

    food = models.CharField(max_length=200)
    music = models.CharField(max_length=200)

    image = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.heropk}. {self.title} - {self.name}"