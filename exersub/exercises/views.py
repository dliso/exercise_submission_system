from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Exercise, Group
from .forms import ExerciseForm, GroupForm

# Create your views here.

def context(ex_pk=None, grp_pk=None, form=None):
    exercises = Exercise.objects.all()
    groups = Group.objects.all()
    cont = {}
    cont['exercises'] = exercises
    cont['groups'] = groups
    if ex_pk:
        cont['active_exercise'] = exercises.get(pk=ex_pk)
        for e in exercises:
            if int(ex_pk) == e.id:
                e.style = 'is-active'
    if grp_pk:
        cont['members'] = groups.get(pk=grp_pk).members.all()
        cont['active_group'] = groups.get(pk=grp_pk)
        for g in groups:
            if int(grp_pk) == g.id:
                g.style = 'is-active'
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
