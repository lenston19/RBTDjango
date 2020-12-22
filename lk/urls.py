from django.urls import path
from . import views

urlpatterns = [
    path('lk/', views.lk, name='lk'),
    path('registration/', views.registration, name='registration'),
]
