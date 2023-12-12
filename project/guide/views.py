from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def tablet(request):
    return render(request, 'tablet.html', {})

def tabletEinrichtung(request):
    return render(request, 'tabletEinrichtung.html', {})

def tabletTeamviewer(request):
    return render(request, 'tabletTeamviewer.html', {})

