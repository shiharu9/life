from django.urls import path

from home.views import *

urlpatterns = [
    path('', home_page),
    path('childhood/', childhood),
    path('youth/', youth),
    path('oldness/', oldness),
    path('add_event', add_event)
]
