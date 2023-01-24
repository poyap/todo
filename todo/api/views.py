from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated 
from ..models import Todo
from .serializers import TodoSerializer

class TodoListCreateAPIView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated, ]
    lookup_field = 'id'

class TodoRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated, ]
    lookup_field = 'id'


