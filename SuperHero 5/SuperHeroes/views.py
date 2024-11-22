from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

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

class HeroUpdateView(UpdateView):
    template_name = "hero/edit.html"
    model = Hero
    fields = '__all__'
    success_url = reverse_lazy('hero_list')

class HeroDeleteView(DeleteView):
    template_name = 'hero/delete.html'
    model = Hero
    success_url = reverse_lazy('hero_list')