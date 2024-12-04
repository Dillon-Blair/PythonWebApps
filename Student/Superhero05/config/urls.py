from django.contrib import admin
from django.urls import path

from SuperHeroes.views import HeroDetailView, HeroListView, HeroCreateView, HeroUpdateView, HeroDeleteView

urlpatterns = [
    path("", HeroListView.as_view()),

    path('hero/',                HeroListView.as_view(),    name='hero_list'),
    path('hero/<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('hero/add',             HeroCreateView.as_view(),  name='hero_add'),
    path('hero/<int:pk>/',       HeroUpdateView.as_view(),  name='hero_edit'),
    path('hero/<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),



    path("admin/", admin.site.urls),
]