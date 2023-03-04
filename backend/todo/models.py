import uuid as uuid_lib
from datetime import timedelta, datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .validators import validate_dead_line


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='todos')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False, 
        unique=True,)
    dead_line = models.DateTimeField(validators=[validate_dead_line,])
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['dead_line']

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('todo:list_view')

    @property
    def days_remained(self):
        """
        Returns days remained for a given deadline.
        :Return: int
        """
        return (self.dead_line.date() - datetime.now().date()).days