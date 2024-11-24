from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, RedirectView
from django.contrib.auth.models import User # Had to import to make user features work. Most of this code I just recycled from the previous projects

from .models import Hero
    
class HeroListView(ListView):
    template_name = 'hero/list.html'
    model = Hero
    context_object_name = 'heroes'

    def get_context_data(self, **kwargs):
        return {
            'object_list': Hero.objects.all()
        }

class HeroDetailView(DetailView):
    template_name = 'hero/detail.html'
    model = Hero
    context_object_name = 'hero'

class HeroCreateView(CreateView):
    template_name = "hero/add.html"
    model = Hero
    fields = '__all__'
    success_url = reverse_lazy('hero_list')

    def form_valid(self, form):
        form.instance.user = get_user(self.request.user)
        return super().form_valid(form)

class HeroUpdateView(UpdateView):
    template_name = "hero/edit.html"
    model = Hero
    fields = '__all__'
    success_url = reverse_lazy('hero_list')

class HeroDeleteView(DeleteView):
    template_name = 'hero/delete.html'
    model = Hero
    success_url = reverse_lazy('hero_list')



### User

def list_heroes(user):
    return dict(heroes=Hero.objects.filter(user=user))


def get_user(user):
    return User.objects.get_or_create(user=user)[0]


class UserAddView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/account_add.html'

class UserHomeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return '/hero/'
        return f'/user/{get_user(self.request.user).pk}'
    
class UserListView(ListView):
    template_name = 'user/list.html'
    model = User

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        return kwargs


class UserDetailView(DetailView):
    template_name = 'user/detail.html'
    model = User

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs.update(list_heroes(kwargs.get('object')))
        return kwargs


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "user/edit.html"
    model = User
    fields = '__all__'
    success_url = reverse_lazy('user_list')