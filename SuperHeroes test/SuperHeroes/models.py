from django.db import models

class Reporter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Hero(models.Model):
    heropk = models.AutoField(primary_key=True) #hero ph
    #reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE, editable=False)

    title = models.CharField(max_length=200) #title
    name = models.CharField(max_length=200) # real name

    strength = models.CharField(max_length=200) #strength 1
    weakness = models.CharField(max_length=200) # strength 2

    age = models.CharField(max_length=200)  # strength 3
    location = models.CharField(max_length=200) # weakness 1

    food = models.CharField(max_length=200) # weakness 2
    music = models.CharField(max_length=200) # weakness 3

    image = models.CharField(max_length=200) # imagepath

    def __str__(self):
        return f"{self.heropk}. {self.title} - {self.name}"