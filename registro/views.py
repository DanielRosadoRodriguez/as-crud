from django.http import HttpResponse
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


def _add_person_to_db(data):
    try:
        person = Persona(
            name=data['name'],
            email=data['email'],
            address=data['address'],
            phone=data['phone'],
        )
        person.save()
    except Exception as e:
        print(f"An error occurred: {e}")


def test_add_person(request):
    data = {
        'name': 'Test',
        'email': 'testo@gmail.com',
        'address': 'Test address',
        'phone': '1234567890',
    }
    _add_person_to_db(data)
    return HttpResponse('Person added to db')
