from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from django.views.generic import RedirectView

from .views_user import UserAddView, UserHomeView, UserUpdateView
from .views_author import AuthorDeleteView, AuthorDetailView, AuthorListView, AuthorUpdateView
from .views_photo import PhotoCarouselView, PhotoDeleteView, PhotoDetailView, PhotoListView, PhotoCreateView, PhotoUpdateView, ArticleCreateView, ArticleDeleteView, ArticleListView, ArticleDetailView, ArticleUpdateView 


urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    
    # Accounts
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),

    #path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article-edit'),

    # User Authentication Paths
    path('',                            RedirectView.as_view(url='author/')), # RedirectView.as_view(url='author/home')),
    path('author/home',                 UserHomeView.as_view(),     name='author_home'),
    path('author/add',                  UserAddView.as_view(),      name='author_add'),
    path('user/<int:pk>/',              UserUpdateView.as_view(),   name='user_edit'),

    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('articles/add/', ArticleCreateView.as_view(), name='article-add'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article-edit'),
    path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),

    # Author Paths
    path('author/',                     AuthorListView.as_view(),    name='author_list'),
    path('author/<int:pk>',             AuthorDetailView.as_view(),  name='author_detail'),
    path('author/<int:pk>/',            AuthorUpdateView.as_view(),  name='author_edit'),
    path('author/<int:pk>/delete',      AuthorDeleteView.as_view(),  name='author_delete'),

    # Photo Paths
    path('photo/carousel',              PhotoCarouselView.as_view()),
    path('photo/',                      PhotoListView.as_view(),    name='photo_list'),
    path('photo/<int:pk>',              PhotoDetailView.as_view(),  name='photo_detail'),
    path('photo/add',                   PhotoCreateView.as_view(),  name='photo_add'),
    path('photo/<int:pk>/',             PhotoUpdateView.as_view(),  name='photo_edit'),
    path('photo/<int:pk>/delete',       PhotoDeleteView.as_view(),  name='photo_delete'),
   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
