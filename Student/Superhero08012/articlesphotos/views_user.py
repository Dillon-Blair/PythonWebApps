from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, RedirectView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm #Default stuff

from .models import Author

#User Authentication Views
class UserHomeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return '/author/'
        author = Author.get_me(self.request.user)
        if author.name == ' ': #if its empty
            author.user.first_name = 'Unknown Author Name'
            author.user.last_name = 'Defualt UserName'
            author.user.email = 'me@unco.us.com'
            author.user.save()
        return f'/author/{author.pk}'


class UserAddView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/add.html'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "registration/edit.html"
    model = User
    fields = ['first_name', 'last_name', 'username', 'email'] #This is included in the editing user settings page
    success_url = reverse_lazy('author_home')