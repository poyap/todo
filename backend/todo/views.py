from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from .models import Todo
from .forms import CreateUpdateTodoForm


class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    paginate_by = 6
    template_name = 'todo/list_view.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(user=self.request.user)
        return qs
    
class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    template_name = 'todo/create_view.html'
    form_class = CreateUpdateTodoForm
    
    def perform_create(self, instance):
        instance.save(user=self.request.user)

class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Todo
    template_name = 'todo/detail_view.html'
    # context_object_name = 'object'
    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     qs = qs.filter(user=self.request.user)
    #     return qs
    
class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    template_name = 'todo/update_view.html'
    form_class = CreateUpdateTodoForm
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
    def get(self, request, *args, **kwargs):
        self.form_class.instance = self.get_object()
        return super().get(self,request)
    
    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     qs = qs.filter(user=self.request.user)
    #     return qs
class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo    
    template_name = 'todo/delete_view.html'
    success_url = reverse_lazy('todo:list_view')
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'