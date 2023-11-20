from django.http import HttpResponse
from django.shortcuts import redirect, render
from registro.models import Persona
from .forms import CreateNewPerson

# Create your views here.

def index(request):
    return render(request, 'index.html')


def users(request):
    return render(request, 'users.html', {'persons': Persona.objects.all()})


def add(request):
    form = CreateNewPerson()
    return render(request, 'add.html', {'form': form})


def get_all_persons(request):
    all_persons = Persona.objects.all()
    persons = list(all_persons)
    for person in persons:
        print(person.name)
    return HttpResponse('Persons listed in console')


def delete_selected_users(request):
    print("función eliminar")
    if request.method == 'POST':
        selected_persons = request.POST.getlist('selected_persons')
        print(selected_persons.count)
        for person_id in selected_persons:
            print(f"Deleting person with id {person_id}")
    return HttpResponse('Persons deleted')


def delete_person(request):
    print("función eliminar")
    if request.method == 'POST':
        person_id = request.POST.get('email')
        print(f"Deleting person with id {person_id}")
    return redirect('users')



def _delete_person(person):
    try:
        person.delete()
    except Exception as e:
        print(f"An error occurred: {e}")


def _add_person_to_db(data):
    try:
        person = Persona(
            name=data['name'],
            email=data['email'],
            address=data['address'],
            phone=data['phone'],
        )
        person.save()
        print(f"Person {person.name} added to db")
    except Exception as e:
        print(f"An error occurred: {e}")


def add_person(request):
    if request.method == 'POST':
        form = CreateNewPerson(request.POST)
        if form.is_valid():
            _add_person_to_db(form.cleaned_data)
    else:
        form = CreateNewPerson()
    return redirect('users')


def test_add_person(request):
    data = {
        'name': 'Test',
        'email': 'testo@gmail.com',
        'address': 'Test address',
        'phone': '1234567890',
    }
    _add_person_to_db(data)
    return HttpResponse('Person added to db')
