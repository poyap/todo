import datetime
from django import template
from ..models import Todo

register = template.Library()
@register.filter
def get_remained_days(obj):
    return obj.days_remained

    