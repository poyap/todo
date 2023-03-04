from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView,)
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission

from .mixins import IsAuthorizedMixin, AuthenticationMixin
from todo.models import Todo
from .serializers import TodoSerializer


class SerilizerClassMixin:
    serializer_class = TodoSerializer

class TodoListCreateAPIView(
    SerilizerClassMixin,
    IsAuthorizedMixin, 
    AuthenticationMixin,
    ListCreateAPIView,):
    def get_queryset(self):
        # print(self.request.headers)
        # print(self.request.auth)
        # print(self.request.META)
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TodoRetriveUpdateDestroyAPIView(
    SerilizerClassMixin,
    IsAuthorizedMixin,
    AuthenticationMixin,
    RetrieveUpdateDestroyAPIView,):

    lookup_url_kwarg = 'uuid'
    lookup_field = 'uuid'

    def get_queryset(self, *args, **kwargs):
        qs = get_object_or_404(Todo, user=self.request.user, uuid=self.kwargs['uuid'])
        print(qs)
        return qs
            