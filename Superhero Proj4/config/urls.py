
from django.contrib.admin import site
from django.urls import path
from django.views.generic import RedirectView

from hero.views import HeroDetailView, HeroListView

urlpatterns = [
    path('admin/', site.urls),

    # Home
    path('', RedirectView.as_view(url='hero/')),

    # Heroes
    path('hero/', HeroListView.as_view()),
    path('hero/<int:id>', HeroDetailView.as_view()),
]