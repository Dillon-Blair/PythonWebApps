from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from SuperHeroes.views import HeroDetailView, HeroListView, HeroCreateView, HeroUpdateView, HeroDeleteView, UserListView, UserHomeView, UserDetailView, UserAddView, UserUpdateView

urlpatterns = [
    path("", RedirectView.as_view(url='hero/')),

    path('hero/',                HeroListView.as_view(),    name='hero_list'),
    path('hero/<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('hero/add',             HeroCreateView.as_view(),  name='hero_add'),
    path('hero/<int:pk>/',       HeroUpdateView.as_view(),  name='hero_edit'),
    path('hero/<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),

    path("admin/", admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/',  RedirectView.as_view(url='/user/home')),

    path('user/',                    UserListView.as_view(),    name='user_list'),
    path('user/home',                UserHomeView.as_view(),    name='user_home'),
    path('user/<int:pk>',            UserDetailView.as_view(),  name='user_detail'),
    path('user/add/',                UserAddView.as_view(),     name='user_add'),
    path('user/<int:pk>/',           UserUpdateView.as_view(),  name='user_edit'),
]