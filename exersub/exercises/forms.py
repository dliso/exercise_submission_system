from django import forms
from django.forms import ModelForm

from .models import Exercise, Group

class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = ['title', 'text']


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['members']
