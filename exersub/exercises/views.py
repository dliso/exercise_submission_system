from django.shortcuts import render
from .models import Exercise

# Create your views here.

def index(request):
    print(request.user)
    exercises = Exercise.objects.all()
    return render(request, 'exercises/index.html', {'exercises': exercises})

def exercise(request, pk):
    exercises = Exercise.objects.all()
    ex = exercises.get(pk=pk)
    ex.style = 'is-active'
    return render(request, 'exercises/exercise.html', {'exercises': exercises,
                                                       'this_ex': ex})
