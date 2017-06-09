from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User

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

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name',
                  'last_name']
