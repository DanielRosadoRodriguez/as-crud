from django import forms

class CreateNewPerson(forms.Form):
    name = forms.CharField(label="Nombre", max_length=200)
    email = forms.EmailField(label="Email", max_length=200)
    address = forms.CharField(label="Dirección", max_length=200)
    phone = forms.CharField(label="Teléfono", max_length=200)
