from django.views.generic import RedirectView #Helps to redirect to the home when going to an empty path
from django.urls import path

from heroes.views import HeroView, HeroListView


urlpatterns = [


    path('', RedirectView.as_view(url='hero/')), #For the homepage when you launch server with an empty path
    path('hero/', HeroListView.as_view()),
    path('hero/<int:id>', HeroView.as_view()),
]
