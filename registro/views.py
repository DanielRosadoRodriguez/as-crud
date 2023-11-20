from django.shortcuts import render
from registro.models import Persona
from .forms import CreateNewPerson

# Create your views here.

def index(request):
    return render(request, 'index.html')


def users(request):
    return render(request, 'users.html')


def add(request):
    form = CreateNewPerson()
    return render(request, 'add.html', {'form': form})


def get_all_persons(request):
    all_persons = Persona.objects.all()
    persons = list(all_persons)
    return persons
