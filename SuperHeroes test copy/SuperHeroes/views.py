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
            return redirect(reverse_lazy('hero-detail'))  # Replace 'home' with your actual URL name

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
            return redirect('hero')  # You can change this if you have a specific login URL
# def list_heroes(user):
#     return dict(heroes=Hero.objects.filter(user=user))


# def get_user(user):
#     return User.objects.get_or_create(user=user)[0]


# class UserAddView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/account_add.html'

# class UserHomeView(RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         if self.request.user.is_anonymous:
#             return '/hero/'
#         return f'/user/{get_user(self.request.user).pk}'
    
# class UserListView(ListView):
#     template_name = 'user/list.html'
#     model = User

#     def get_context_data(self, **kwargs):
#         kwargs = super().get_context_data(**kwargs)
#         return kwargs


# class UserDetailView(DetailView):
#     template_name = 'user/detail.html'
#     model = User

#     def get_context_data(self, **kwargs):
#         kwargs = super().get_context_data(**kwargs)
#         kwargs.update(list_heroes(kwargs.get('object')))
#         return kwargs


# class UserUpdateView(LoginRequiredMixin, UpdateView):
#     template_name = "user/edit.html"
#     model = User
#     fields = '__all__'
#     success_url = reverse_lazy('user_list')