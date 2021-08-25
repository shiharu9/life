from django.forms import ModelForm, forms
from .models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'content', 'period')
