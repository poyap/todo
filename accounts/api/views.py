from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserListCreateAPIView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAdminUser,]
    lookup_field = 'id'

class UserRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAdminUser,]
    lookup_field = 'id'