from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy

# Author models
class Author(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    biography = models.TextField()

    def __str__(self):
        return f'{self.user.username}'

    def get_absolute_url(self):
        return reverse_lazy('author_detail', args=[str(self.id)])

    @property
    def name(self):
        return self.user.first_name + ' ' + self.user.last_name

    #For the photos
    @property
    def photos(self):
        return Photo.objects.filter(author=self)

    @staticmethod
    def get_me(user):
        if user.is_authenticated:
            return Author.objects.get_or_create(user=user)[0]
        else:
           return reverse_lazy('author_detail')


def get_upload(instance, filename):
    return f'images/{filename}'

# Article Model
class Article(models.Model):
    
    hero = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE, null=True, blank=True)
    

# Photo Models
class Photo (models.Model):

    author = models.ForeignKey(Author, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to=get_upload)

    def __str__(self):
        return f'{self.pk} - {self.title}'

    def get_absolute_url(self):
        return reverse_lazy('photo_detail', args=[str(self.id)])
