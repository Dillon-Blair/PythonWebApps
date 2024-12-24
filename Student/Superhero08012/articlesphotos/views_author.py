from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Author

#CRUD OPERATIONS
class AuthorView(RedirectView):
    url = reverse_lazy('author_list')


class AuthorListView(ListView):
    template_name = 'author/list.html'
    model = Author
    context_object_name = 'authors'


class AuthorDetailView(DetailView):
    template_name = 'author/detail.html'
    model = Author
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
            kwargs = super().get_context_data(**kwargs)
            author = kwargs.get('author')
            kwargs.update(dict(photos=author.photos))
            return 

class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "author/edit.html"
    model = Author
    fields = '__all__'


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    template_name = 'author/delete.html'
    success_url = reverse_lazy('author_list')
