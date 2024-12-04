from django.contrib.admin import site
from django.urls import path
from django.views.generic import RedirectView #For HomePage redirect

from hero.views import HeroView, HeroListView

urlpatterns = [
    path('admin/', site.urls), #For the admin Portal 


    path('', RedirectView.as_view(url='hero/')), #For the HomePage when path is empty 
    path('hero/', HeroListView.as_view()),
    path('hero/<int:id>', HeroView.as_view()), #For the String form
]