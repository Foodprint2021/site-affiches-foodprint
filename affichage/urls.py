from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_crous, name='liste_crous'),
]