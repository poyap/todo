from django import template
from ..models import Todo
import datetime

register = template.Library()
@register.filter
def get_remained_days(obj):
    return obj.calculate_days_remained()

    