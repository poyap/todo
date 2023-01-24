from django.core.exceptions import ValidationError
import datetime

def validate_dead_line(value):
    if value.date() <= datetime.date.today():
        raise ValidationError('You can not choose a passed date.')