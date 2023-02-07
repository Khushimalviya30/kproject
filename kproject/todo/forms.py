from dataclasses import fields
from pyexpat import model
from django import forms
from todo.models import Todo
from todo.models import Contact

class Todoform(forms.ModelForm):
    class Meta():
        model=Todo
        fields={"title","description","name","email"}

class contactform(forms.ModelForm):
    class Meta():
        model=Contact
        fields={"name","Sub","messg","email"}