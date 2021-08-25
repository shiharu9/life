from django.shortcuts import render
from django.contrib import staticfiles

from .models import Event
from .forms import EventForm
# Create your views here.


def home_page(request):
    data = "Hello"
    return render(request, 'home/home_page.html', {'data': data})


def childhood(request):
    data = Event.objects.filter(period__name='Детство')
    return render(request, 'home/childhood.html', {'data': data})


def youth(request):
    data = Event.objects.filter(period__name='Молодость')
    return render(request, 'home/youth.html', {'data': data})


def oldness(request):
    data = Event.objects.filter(period__name='Старость')
    return render(request, 'home/oldness.html', {'data': data})


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'home/add_event.html', {'form': EventForm()})

