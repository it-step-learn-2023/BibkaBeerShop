from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('home', index),
    path('about', about),
    path('contacts', contacts),
]
