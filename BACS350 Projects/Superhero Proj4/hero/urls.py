from django.contrib.admin import site
from django.views.generic import RedirectView
from django.urls import path

from hero.views import HeroDetailView, HeroListView

urlpatterns = [

    path('', RedirectView.as_view(url='heroview/')),
    path('heroview/', HeroListView.as_view()),
    path('heroview/<int:id>', HeroDetailView.as_view()),

    path(r'admin/', site.urls),
]