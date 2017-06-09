from django import forms
from django.forms import ModelForm

from .models import Exercise, Group, Handin

class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = ['title', 'text']


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['members']


class HandinForm(ModelForm):
    class Meta:
        model = Handin
        fields = ['text']
