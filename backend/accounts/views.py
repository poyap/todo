from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm


class UserRegisterView(CreateView):
    template_name = 'registration/register.html'
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    
class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/account_detail.html'
    model = User
    context_object_name = 'object'

    def get_object(self):
        return self.request.user
    

class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/account_update.html'
    model = User
    fields = ['username', 'email']
    success_url = reverse_lazy('accounts:account_detail')

    def get_object(self):
        return self.request.user

class UserDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'accounts/account_delete.html'
    model = User
    success_url = reverse_lazy('accounts:account_register')

    def get_object(self):
        return self.request.user

    


