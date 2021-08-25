from django.shortcuts import render

from .models import Event
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
