from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class CUser(models.Model):
    # 'Custom User'
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @classmethod
    def make(cls, username, password, email, first_name, last_name):
        new_user = User(username=username, password=password, email=email,
                        first_name=first_name, last_name=last_name)
        new_user.save()
        print(new_user)
        new_cuser = cls(user=new_user)
        new_cuser.save()
        return new_cuser

    def __str__(self):
        return self.user.username


class Group(models.Model):
    creator = models.ForeignKey(CUser, related_name='creator_of')
    members = models.ManyToManyField(CUser, related_name='member_of')
    creation_date = models.DateTimeField(auto_now=True)


class Handin(models.Model):
    creator = models.ForeignKey(CUser)
    group = models.ForeignKey(Group, null=True, blank=True)
    evaluator_group = models.ForeignKey(Group, related_name='evaluator_of', null=True, blank=True)
    evaluation = models.ForeignKey('Evaluation', blank=True, null=True)
    handin_date = models.DateTimeField(auto_now=True)
    text = models.TextField()
    exercise = models.ForeignKey('Exercise')

    def __str__(self):
        s = self.text
        s2 = s if len(s) < 50 else s[47] + '...'
        return self.exercise.title + ': ' + s2


class Evaluation(models.Model):
    group = models.ForeignKey(Group)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now=True)


class Exercise(models.Model):
    author = models.ForeignKey(CUser)
    creation_date = models.DateTimeField(auto_now=True)
    text = models.TextField()
    title = models.CharField(max_length=200)

    style = ''

    def __str__(self):
        return self.title
