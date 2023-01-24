from django.db import models
from django.contrib.auth.models import User
from .validators import validate_dead_line
from django.urls import reverse
from datetime import timedelta, datetime

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='todos')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
    dead_line = models.DateTimeField(validators=[validate_dead_line,])
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-dead_line']

    def get_absolute_url(self):
        return reverse('todo:list_view')

    
    def calculate_days_remained(self):
        delta = self.dead_line.date() - datetime.now().date()
        return delta.days