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


# TODO
def delete_selected_users(request):
    if request.method == 'POST':
        selected_persons = request.POST.getlist('checks[]')
        for person_id in selected_persons:
            person_to_delete = Persona.objects.get(email=person_id)
            _delete_person(person_to_delete)
    return redirect('users')


def delete_person(request):
    if request.method == 'POST':
        person_id = request.POST.get('email')
        person_to_delete = Persona.objects.get(email=person_id)
        _delete_person(person_to_delete)
        print(f"Deleting person with id {person_id}")
    return redirect('users')


def _delete_person(person):
    try:
        person.delete()
    except Exception as e:
        print(f"An error occurred: {e}")


def edit(request):
    if request.method == 'POST':
        person_id = request.POST.get('email')
        person_to_edit = Persona.objects.get(email=person_id)
        form = CreateNewPerson(
            initial={
                'name': person_to_edit.name,
                'email': person_to_edit.email,
                'address': person_to_edit.address,
                'phone': person_to_edit.phone,
            }
        )
        return render(request, 'edit.html', {'form': form})
    return HttpResponse('Error al editar')


def edit_person(request):
    if request.method == 'POST':
        person_id = request.POST.get('email')
        person_to_edit = Persona.objects.get(email=person_id)
        form = CreateNewPerson(request.POST)
        if form.is_valid():
            _edit_person(person_to_edit, form.cleaned_data)
    return redirect('users')

def _edit_person(person, new_person):
    try:
        _delete_person(person)
        _add_person_to_db(new_person)
        print(f"Person {new_person.name} edited")
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
