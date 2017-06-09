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
    group = models.ForeignKey(Group)
    evaluator_group = models.ForeignKey(Group, related_name='evaluator_of')
    evaluation = models.ForeignKey('Evaluation')
    handin_date = models.DateTimeField(timezone.now())
    text = models.TextField()
    exercise = models.ForeignKey('Exercise')


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
