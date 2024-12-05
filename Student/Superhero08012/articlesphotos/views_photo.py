from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, TemplateView, UpdateView
from django.core.exceptions import PermissionDenied
from .models import Author, Photo, Article


#Article Views included in Photo Views
class ArticleListView(ListView):
    model = Article
    template_name = 'article/list.html'
    context_object_name = 'articles'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article/add.html'
    fields = ['hero','title', 'content', 'author','photo']
    success_url = reverse_lazy('article-list')


    def form_valid(self, form):
        # Set value to current user
        form.instance.author = self.request.user.username
        return super().form_valid(form)

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/detail.html'
    context_object_name = 'article'

#Must be logged in
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'article/edit.html'
    success_url = reverse_lazy('article-list')
    fields = ['hero','title', 'content', 'author','photo']
    def get_object(self, queryset=None):
        article = super().get_object(queryset)

        # User Authentication
        if article.author != self.request.user.username:
            raise PermissionDenied("You do not have permission to delete this object.")

        return article
    
#Must be logged in 
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article/delete.html'
    success_url = reverse_lazy('article-list')

    def get_object(self, queryset=None):
        article = super().get_object(queryset)

        # User Authentication
        if article.author != self.request.user.username:
            raise PermissionDenied("You do not have permission to delete this object.")

        return article

#Photo Views

class PhotoView(RedirectView):
    url = reverse_lazy('photo_list')


class PhotoListView(ListView):
    template_name = 'photo/list.html'
    model = Photo
    context_object_name = 'photos'


class PhotoCarouselView(TemplateView):
    template_name = 'photo/carousel.html'

    def get_context_data(self, **kwargs):
        photos = Author.get_me(self.request.user).photos
        carousel = carousel_data(photos)
        return dict(title='Carousel View', carousel=carousel)


def carousel_data(photos):

    def photo_data(id, image):
        x = dict(image_url=f"/media/{image}", id=str(id), label=f"{image} {id}")
        if id == 0:
            x.update(active="active", aria='aria-current="true"')
        return x

    return [photo_data(id, photo.image) for id, photo in enumerate(photos)]


class PhotoDetailView(DetailView):
    template_name = 'photo/detail.html'
    model = Photo
    context_object_name = 'photo'


class PhotoCreateView(LoginRequiredMixin, CreateView):
    template_name = "photo/add.html"
    model = Photo
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = Author.get_me(self.request.user)
        return super().form_valid(form)


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "photo/edit.html"
    model = Photo
    fields = '__all__'


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'photo/delete.html'
    success_url = reverse_lazy('photo_list')
