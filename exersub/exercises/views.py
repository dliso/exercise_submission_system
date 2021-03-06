from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from .models import Exercise, Group, Handin, CUser
from .forms import ExerciseForm, GroupForm, HandinForm, LoginForm, SignupForm

# Create your views here.

def context(ex_pk=None, grp_pk=None, form=None):
    exercises = Exercise.objects.all()
    groups = Group.objects.all()
    cont = {}
    cont['exercises'] = exercises
    cont['groups'] = groups
    if ex_pk == 'latest':
        ex = exercises.latest('creation_date')
        cont['active_exercise'] = ex
        ex_pk = ex.id
    if ex_pk:
        ex = exercises.get(pk=ex_pk)
        cont['active_exercise'] = ex
        for e in exercises:
            if int(ex_pk) == e.id:
                e.style = 'is-active'
        try:
            current_handin = Handin.objects.filter(exercise__id=ex_pk).latest('handin_date')
            cont['current_handin'] = current_handin
        except:
            pass
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
    return render(request, 'exercises/exercise.html', context(ex_pk='latest'))

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
            return HttpResponseRedirect('/exercise/' + str(new_ex.id))
    else:
        form = ExerciseForm()
    return render(request, 'exercises/add_exercise.html', context(form=form))

def hand_in_exercise(request, ex_pk):
    if request.method == 'POST':
        form = HandinForm(request.POST)
        if form.is_valid():
            handin = Handin(
                creator=request.user.cuser,
                text=form.cleaned_data['text'],
                exercise= Exercise.objects.get(id=ex_pk)
            )
            handin.save()
            return HttpResponseRedirect('/exercise/' + ex_pk)
    else:
        form = HandinForm()
    return render(request, 'exercises/hand_in_exercise.html', context(ex_pk=ex_pk, form=form))

def logout(request):
    logout()
    return HttpResponseRedirect('/')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_cuser = CUser(user=new_user)
            new_cuser.save()
            login(request, new_user)
            return HttpResponseRedirect('/')
    form = SignupForm()
    return render(request, 'registration/signup.html', context(form=form))
