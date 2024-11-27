from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from SuperHeroes.views import profile_view, SignUpView, HeroDetailView, HeroListView, HeroCreateView, HeroUpdateView, HeroDeleteView # UserListView, UserHomeView, UserDetailView, UserAddView, UserUpdateView

urlpatterns = [
    path("", RedirectView.as_view(url='hero/')),

    path('hero/',                HeroListView.as_view(),    name='hero_list'),
    path('hero/<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('hero/add',             HeroCreateView.as_view(),  name='hero_add'),
    path('hero/<int:pk>/',       HeroUpdateView.as_view(),  name='hero_edit'),
    path('hero/<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),

    path("admin/", admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/profile/', HeroListView.as_view(), name='hero_list'),

]