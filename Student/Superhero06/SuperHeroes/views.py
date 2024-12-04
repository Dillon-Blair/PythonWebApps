from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, RedirectView
from django.contrib.auth.models import User # Had to import to make user features work. Most of this code I just recycled from the previous projects
from django.shortcuts import redirect
from django.contrib.auth import login
from .models import Hero
from django.views import View
from django.shortcuts import render
#from .models import Reporter


#CRUD Operation Views  
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
        form.instance.reporter = self.request.user
        form.instance.user = self.request.user
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



### User Authentication 

class SignUpView(View):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect(reverse_lazy('hero_list'))  # Replace 'home' with your actual URL name

        return render(request, self.template_name, {'form': form})

class profile_view(View):
    # Get the current user
    def profile():
        user = request.user
        
        # If the user is authenticated, show their profile
        if user.is_authenticated:
            return render(request, 'accounts/profile.html', {'user': user})
        else:
            # Redirect to login if not authenticated
            return redirect('hero_list')  # You can change this if you have a specific login URL
