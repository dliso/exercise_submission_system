from django.contrib import admin

from .models import CUser, Exercise, Group

# Register your models here.

admin.site.register(CUser)
admin.site.register(Exercise)
admin.site.register(Group)
