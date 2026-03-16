from django.shortcuts import render
from .models import Person

def index(request):
    persons = Person.objects.all()
    return render(request, 'index.html', {'persons': persons})