from django.shortcuts import render
from .forms import CreateNewPerson
# Create your views here.

def index(request):
    return render(request, 'index.html')


def users(request):
    return render(request, 'users.html')

def add(request):
    form = CreateNewPerson()
    return render(request, 'add.html', {'form': form})