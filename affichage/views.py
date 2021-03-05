from django.shortcuts import render, get_object_or_404
from .models import Affiche

def liste_crous(request):
    affiches = Affiche.objects.filter()
    return render(request, 'affichage/liste_crous.html', {'affiches' : affiches})