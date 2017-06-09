from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Exercise
from .forms import ExerciseForm

# Create your views here.

def context(ex_pk=None, form=None):
    exercises = Exercise.objects.all()
    cont = {}
    cont['exercises'] = exercises
    if ex_pk:
        cont['active_exercise'] = exercises.get(pk=ex_pk)
    if form:
        cont['form'] = form
    return cont

def index(request):
    return render(request, 'exercises/index.html', context())

def exercise(request, pk):
    # ex.style = 'is-active'
    return render(request, 'exercises/exercise.html', context(ex_pk=pk))

def add_exercise(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            new_ex = Exercise(author=request.user.cuser,
                              text=form.cleaned_data['text'],
                              title=form.cleaned_data['title'])
            new_ex.save()
            return HttpResponseRedirect('/')
    else:
        form = ExerciseForm()
    return render(request, 'exercises/add_exercise.html', context(form=form))
